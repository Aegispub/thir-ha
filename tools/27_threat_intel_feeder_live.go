/*
Tool_27 Extract_attacker_IPs_from_IR_cases
// 27_threat_intel_feeder_live.go
//
// THIR LIVE PIPELINE — PRODUCTION TOOL
// Adapted from: InfraReadyPortfolio/06_soc_collaboration_tools/27_threat_intelligence_feeder/
//
// CHANGES FROM ORIGINAL (threat_intelligence_feeder.go):
//   1. IOC struct extended: added AbuseScore, Country, ISP, OTXPulses, LastSeen fields
//   2. readThreatIntel() removed — replaced with readIPsFromFile() (plain IP list, one per line)
//      WHY: Cowrie pipeline produces attacker IP list, not CSV intel feed files
//      KEPT: same os.Open/defer/scanner/error handling pattern
//   3. consolidateIOCs() preserved AS-IS — dedup logic correct, works on IP as Indicator
//   4. writeIOCs() (CSV stdout) removed — replaced with writeEnrichedJSON() to output file
//   5. enrichIP() NEW — AbuseIPDB /v2/check API call, extracts score/country/ISP
//   6. enrichOTX() NEW — AlienVault OTX IPv4 general API, extracts pulse count
//   7. enrichAll() NEW — concurrent enrichment via goroutines + channel (same pattern as 05_network_monitor_live.go)
//   8. main() extended: --input, --output flags; ABUSEIPDB_API_KEY, OTX_API_KEY from env
//   9. All logInfo/logWarning/fatalError helpers preserved unchanged
//
// ROLE IN THIR PIPELINE:
//   Reads attacker IP list extracted from data/ir_cases.json by cowrie_parser.
//   Enriches each IP via AbuseIPDB (abuse score, country, ISP) and OTX (pulse count).
//   Deduplicates IPs across sessions.
//   Writes data/threat_ips.json → portfolio threat map and IR case cards read it live.
//
// GITHUB ACTIONS USAGE:
//   go run tools/27_threat_intel_feeder_live.go \
//     --input /tmp/attacker_ips.txt \
//     --output data/threat_ips.json
//
// ENV VARS (set as GitHub Actions secrets):
//   ABUSEIPDB_API_KEY  — from abuseipdb.com free account (1000 checks/day)
//   OTX_API_KEY        — from otx.alienvault.com free account
//   Both are optional — tool runs without them, enrichment fields default to zero/unknown
//
// OUTPUT FORMAT (data/threat_ips.json):
//   {
//     "generated_at": "2025-01-15T11:00:00Z",
//     "total_ips": 2,
//     "ips": [
//       {
//         "indicator": "185.220.101.5",
//         "type": "ip",
//         "abuse_score": 100,
//         "country": "DE",
//         "isp": "Tor Project",
//         "asn": "AS14061",
//         "asn_name": "DigitalOcean, LLC",
//         "org": "AS14061 DigitalOcean, LLC",
//         "is_tor": false,
//         "is_proxy": false,
//         "is_vpn": false,
//         "otx_pulses": 47,
//         "last_seen": "2025-01-15T11:00:01Z"
//       }
//     ]
//   }

*/

package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"sync"
	"time"
)

// IOC represents a single enriched attacker IP.
// Original fields (Indicator, Type) preserved.
// New fields added for AbuseIPDB and OTX enrichment.
type IOC struct {
	Indicator  string `json:"indicator"`
	Type       string `json:"type"`
	AbuseScore int    `json:"abuse_score"`
	Country    string `json:"country"`
	ISP        string `json:"isp"`
	ASN        string `json:"asn"`
	ASNName    string `json:"asn_name"`
	Org        string `json:"org"`
	IsTor      bool   `json:"is_tor"`
	IsProxy    bool   `json:"is_proxy"`
	IsVPN      bool   `json:"is_vpn"`
	OTXPulses  int    `json:"otx_pulses"`
	LastSeen   string `json:"last_seen"`
}

// ThreatIPReport is the JSON structure written to data/threat_ips.json
type ThreatIPReport struct {
	GeneratedAt string `json:"generated_at"`
	TotalIPs    int    `json:"total_ips"`
	IPs         []IOC  `json:"ips"`
}

// CorpusEntry represents the subset of Tool 43's enriched_corpus.json
// fields relevant to deciding whether an IP needs re-enrichment. Only
// the fields this tool actually reads are declared -- extra fields in
// the real corpus (session_count, ttps_observed, etc.) are ignored by
// Go's json.Unmarshal, not an error.
type CorpusEntry struct {
	AbuseScore       int    `json:"abuse_score"`
	Country          string `json:"country"`
	ISP              string `json:"isp"`
	Org              string `json:"org"`
	IsTor            bool   `json:"is_tor"`
	IsProxy          bool   `json:"is_proxy"`
	IsVPN            bool   `json:"is_vpn"`
	OTXPulses        int    `json:"otx_pulses"`
	EnrichedAt       string `json:"enriched_at"`
	EnrichmentTTLDays int   `json:"enrichment_ttl_days"`
}

// loadEnrichedCorpus reads Tool 43's data/enriched_corpus.json (this tool
// never writes to it -- read-only, matching the isolation contract
// documented in enriched_corpus.yml). A missing or unreadable corpus file
// degrades gracefully to an empty map, meaning every IP is treated as
// needing enrichment -- correct behaviour for a first-ever run before the
// corpus workflow has produced anything yet.
func loadEnrichedCorpus(path string) map[string]CorpusEntry {
	corpus := make(map[string]CorpusEntry)

	data, err := os.ReadFile(path)
	if err != nil {
		logInfo("No enriched corpus found at %s -- all IPs will be enriched (cache disabled or first run)", path)
		return corpus
	}

	if err := json.Unmarshal(data, &corpus); err != nil {
		logWarning("Could not parse enriched corpus at %s: %v -- proceeding without cache", path, err)
		return make(map[string]CorpusEntry)
	}

	logInfo("Loaded enriched corpus from %s (%d known IPs)", path, len(corpus))
	return corpus
}

// isCacheFresh reports whether a corpus entry's enrichment is still
// within its TTL window, meaning AbuseIPDB/ipinfo.io/OTX should NOT be
// called again for this IP. Mirrors the exact TTL logic already
// implemented in tools/43_enriched_corpus.py's needs_reenrichment() --
// same cutoff computation, same "missing enriched_at means treat as
// stale" default, kept independently here since this is Go and that is
// Python, but the semantics are identical by design.
func isCacheFresh(entry CorpusEntry, now time.Time) bool {
	if entry.EnrichedAt == "" {
		return false
	}
	enrichedAt, err := time.Parse(time.RFC3339, entry.EnrichedAt)
	if err != nil {
		return false
	}
	ttlDays := entry.EnrichmentTTLDays
	if ttlDays <= 0 {
		ttlDays = 30 // matches TTL_DAYS_DEFAULT in tools/43_enriched_corpus.py
	}
	ageDays := now.Sub(enrichedAt).Hours() / 24.0
	return ageDays < float64(ttlDays)
}

// applyCachedValues copies a corpus entry's reputation fields onto an
// IOC, used when a cache hit means the API calls are skipped entirely
// for this run. LastSeen is still updated to "now" -- this tool's own
// run is a legitimate observation of the IP even when the underlying
// reputation data is reused from cache.
func applyCachedValues(ioc IOC, entry CorpusEntry) IOC {
	ioc.AbuseScore = entry.AbuseScore
	ioc.Country = entry.Country
	ioc.ISP = entry.ISP
	ioc.Org = entry.Org
	ioc.IsTor = entry.IsTor
	ioc.IsProxy = entry.IsProxy
	ioc.IsVPN = entry.IsVPN
	ioc.OTXPulses = entry.OTXPulses
	return ioc
}

// AbuseIPDB API response shapes (only fields we use)
type abuseIPDBResponse struct {
	Data struct {
		AbuseConfidenceScore int    `json:"abuseConfidenceScore"`
		CountryCode          string `json:"countryCode"`
		ISP                  string `json:"isp"`
	} `json:"data"`
}

// ipinfo.io API response shape (no key required for basic lookups)
type ipinfoResponse struct {
	Org     string `json:"org"` // "AS14061 DigitalOcean, LLC"
	Privacy struct {
		VPN   bool `json:"vpn"`
		Proxy bool `json:"proxy"`
		Tor   bool `json:"tor"`
	} `json:"privacy"`
}

// OTX API response shape (only fields we use)
type otxResponse struct {
	PulseInfo struct {
		Count int `json:"count"`
	} `json:"pulse_info"`
}

var verbose bool

// ---------------------------
// Logging Helpers (unchanged from original)
// ---------------------------

func logInfo(format string, args ...interface{}) {
	if !verbose {
		return
	}
	fmt.Fprintf(os.Stderr, "[INFO] "+format+"\n", args...)
}

func logWarning(format string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, "[WARNING] "+format+"\n", args...)
}

func fatalError(format string, args ...interface{}) {
	fmt.Fprintf(os.Stderr, "[ERROR] "+format+"\n", args...)
	os.Exit(1)
}

// ---------------------------
// IP List Reader (replaces readThreatIntel)
// ---------------------------

// readIPsFromFile reads a plain text file of IP addresses, one per line.
// Replaces readThreatIntel() — same os.Open/defer/scanner/error pattern preserved.
// Each IP becomes an IOC with Type="ip" ready for consolidation and enrichment.
func readIPsFromFile(path string) ([]IOC, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("failed to open IP list %s: %w", path, err)
	}
	defer file.Close()

	var iocs []IOC
	scanner := bufio.NewScanner(file)
	lineNum := 0

	for scanner.Scan() {
		lineNum++
		ip := strings.TrimSpace(scanner.Text())
		if ip == "" || strings.HasPrefix(ip, "#") {
			continue
		}
		iocs = append(iocs, IOC{
			Indicator: ip,
			Type:      "ip",
		})
	}

	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("error reading IP list %s: %w", path, err)
	}

	logInfo("Read %d IP(s) from %s", len(iocs), path)
	return iocs, nil
}

// ---------------------------
// Deduplication (preserved AS-IS from original)
// ---------------------------

// consolidateIOCs deduplicates IOCs by Indicator value.
// UNCHANGED from original — same map-based dedup, same type-conflict warning.
func consolidateIOCs(allIOCs []IOC) []IOC {
	seen := make(map[string]IOC)
	for _, ioc := range allIOCs {
		if existing, ok := seen[ioc.Indicator]; ok {
			if existing.Type != ioc.Type && ioc.Type != "" {
				logWarning(
					"Duplicate indicator '%s' with differing types ('%s' vs '%s'); keeping first",
					ioc.Indicator,
					existing.Type,
					ioc.Type,
				)
			}
			continue
		}
		seen[ioc.Indicator] = ioc
	}

	result := make([]IOC, 0, len(seen))
	for _, ioc := range seen {
		result = append(result, ioc)
	}
	return result
}

// ---------------------------
// API Enrichment (new)
// ---------------------------

// enrichIP calls AbuseIPDB /v2/check for a single IP.
// Returns updated IOC with AbuseScore, Country, ISP populated.
// Falls back gracefully — returns original IOC unchanged on any error.
func enrichIP(ioc IOC, apiKey string, client *http.Client) IOC {
	if apiKey == "" {
		logInfo("AbuseIPDB key not set — skipping enrichment for %s", ioc.Indicator)
		return ioc
	}

	url := fmt.Sprintf(
		"https://api.abuseipdb.com/api/v2/check?ipAddress=%s&maxAgeInDays=90",
		ioc.Indicator,
	)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		logWarning("AbuseIPDB request build failed for %s: %v", ioc.Indicator, err)
		return ioc
	}
	req.Header.Set("Key", apiKey)
	req.Header.Set("Accept", "application/json")

	resp, err := client.Do(req)
	if err != nil {
		logWarning("AbuseIPDB request failed for %s: %v", ioc.Indicator, err)
		return ioc
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		logWarning("AbuseIPDB returned HTTP %d for %s", resp.StatusCode, ioc.Indicator)
		return ioc
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		logWarning("AbuseIPDB read failed for %s: %v", ioc.Indicator, err)
		return ioc
	}

	var parsed abuseIPDBResponse
	if err := json.Unmarshal(body, &parsed); err != nil {
		logWarning("AbuseIPDB parse failed for %s: %v", ioc.Indicator, err)
		return ioc
	}

	ioc.AbuseScore = parsed.Data.AbuseConfidenceScore
	ioc.Country = parsed.Data.CountryCode
	ioc.ISP = parsed.Data.ISP

	logInfo("AbuseIPDB: %s → score=%d country=%s isp=%s",
		ioc.Indicator, ioc.AbuseScore, ioc.Country, ioc.ISP)
	return ioc
}

// enrichASN calls ipinfo.io for ASN, org, and anonymous-infrastructure flags.
// No API key required (free tier: 50K lookups/month).
// Falls back gracefully — leaves ASN fields empty on any error.
func enrichASN(ioc IOC, client *http.Client) IOC {
	url := fmt.Sprintf("https://ipinfo.io/%s/json", ioc.Indicator)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil { return ioc }
	req.Header.Set("Accept", "application/json")

	resp, err := client.Do(req)
	if err != nil { return ioc }
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK { return ioc }

	body, err := io.ReadAll(resp.Body)
	if err != nil { return ioc }

	var parsed ipinfoResponse
	if err := json.Unmarshal(body, &parsed); err != nil { return ioc }

	ioc.Org = parsed.Org
	if parsed.Org != "" {
		parts := strings.SplitN(parsed.Org, " ", 2)
		if len(parts) == 2 {
			ioc.ASN     = parts[0]
			ioc.ASNName = parts[1]
		} else {
			ioc.ASN = parsed.Org
		}
	}
	ioc.IsTor   = parsed.Privacy.Tor
	ioc.IsProxy = parsed.Privacy.Proxy
	ioc.IsVPN   = parsed.Privacy.VPN

	logInfo("ipinfo: %s → asn=%s name=%s tor=%v proxy=%v vpn=%v",
		ioc.Indicator, ioc.ASN, ioc.ASNName, ioc.IsTor, ioc.IsProxy, ioc.IsVPN)
	return ioc
}

// enrichOTX calls AlienVault OTX IPv4 general endpoint for a single IP.
// Returns updated IOC with OTXPulses populated.
// Falls back gracefully on any error.
func enrichOTX(ioc IOC, apiKey string, client *http.Client) IOC {
	if apiKey == "" {
		logInfo("OTX key not set — skipping OTX enrichment for %s", ioc.Indicator)
		return ioc
	}

	url := fmt.Sprintf(
		"https://otx.alienvault.com/api/v1/indicators/IPv4/%s/general",
		ioc.Indicator,
	)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		logWarning("OTX request build failed for %s: %v", ioc.Indicator, err)
		return ioc
	}
	req.Header.Set("X-OTX-API-KEY", apiKey)

	resp, err := client.Do(req)
	if err != nil {
		logWarning("OTX request failed for %s: %v", ioc.Indicator, err)
		return ioc
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		logWarning("OTX returned HTTP %d for %s", resp.StatusCode, ioc.Indicator)
		return ioc
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		logWarning("OTX read failed for %s: %v", ioc.Indicator, err)
		return ioc
	}

	var parsed otxResponse
	if err := json.Unmarshal(body, &parsed); err != nil {
		logWarning("OTX parse failed for %s: %v", ioc.Indicator, err)
		return ioc
	}

	ioc.OTXPulses = parsed.PulseInfo.Count
	logInfo("OTX: %s → pulses=%d", ioc.Indicator, ioc.OTXPulses)
	return ioc
}

// enrichAll enriches all IOCs concurrently via goroutines.
// Uses same goroutine+channel pattern as 05_network_monitor_live.go.
// 50ms stagger between launches to respect AbuseIPDB rate limits.
func enrichAll(iocs []IOC, abuseKey, otxKey string, corpus map[string]CorpusEntry) []IOC {
	client := &http.Client{Timeout: 8 * time.Second}
	results := make(chan IOC, len(iocs))
	var wg sync.WaitGroup
	now := time.Now().UTC()

	var cacheHits, freshEnrichments int
	var statsMu sync.Mutex

	for _, ioc := range iocs {
		wg.Add(1)
		go func(i IOC) {
			defer wg.Done()

			if entry, known := corpus[i.Indicator]; known && isCacheFresh(entry, now) {
				i = applyCachedValues(i, entry)
				i.LastSeen = now.Format(time.RFC3339)
				statsMu.Lock()
				cacheHits++
				statsMu.Unlock()
				results <- i
				return
			}

			i = enrichIP(i, abuseKey, client)
			i = enrichASN(i, client)
			i = enrichOTX(i, otxKey, client)
			i.LastSeen = now.Format(time.RFC3339)
			statsMu.Lock()
			freshEnrichments++
			statsMu.Unlock()
			results <- i
		}(ioc)
		time.Sleep(50 * time.Millisecond) // respect AbuseIPDB 1000/day free tier
	}

	// Close results channel once all goroutines finish
	go func() {
		wg.Wait()
		close(results)
	}()

	var enriched []IOC
	for ioc := range results {
		enriched = append(enriched, ioc)
	}

	logInfo("Enrichment complete — cache hits: %d, fresh API enrichments: %d", cacheHits, freshEnrichments)
	return enriched
}

// ---------------------------
// JSON Output (replaces writeIOCs CSV)
// ---------------------------

// writeEnrichedJSON writes the enriched IP report to data/threat_ips.json.
// Replaces writeIOCs() — same role, JSON output for portfolio dashboard.
func writeEnrichedJSON(iocs []IOC, outputPath string) error {
	report := ThreatIPReport{
		GeneratedAt: time.Now().UTC().Format(time.RFC3339),
		TotalIPs:    len(iocs),
		IPs:         iocs,
	}

	data, err := json.MarshalIndent(report, "", "  ")
	if err != nil {
		return fmt.Errorf("failed to marshal JSON: %w", err)
	}

	if err := os.WriteFile(outputPath, data, 0644); err != nil {
		return fmt.Errorf("failed to write %s: %w", outputPath, err)
	}
	return nil
}

// ---------------------------
// Main Entry Point
// ---------------------------

func main() {
	inputFile := flag.String("input", "", "Path to plain-text attacker IP list (one IP per line)")
	outputFile := flag.String("output", "data/threat_ips.json", "Path to write enriched threat IPs JSON")
	corpusFile := flag.String("corpus", "data/enriched_corpus.json",
		"Path to Tool 43's enriched_corpus.json, used as a TTL-based cache to skip "+
			"AbuseIPDB/ipinfo.io/OTX calls for IPs enriched within their TTL window. "+
			"Pass an empty string to disable caching entirely.")
	flag.BoolVar(&verbose, "verbose", false, "Enable verbose output")
	flag.BoolVar(&verbose, "v", false, "Enable verbose output (shorthand)")
	flag.Parse()

	if strings.TrimSpace(*inputFile) == "" {
		fatalError("Missing required argument: --input (path to IP list file)")
	}

	// Read API keys from environment — set as GitHub Actions secrets
	abuseKey := os.Getenv("ABUSEIPDB_API_KEY")
	otxKey := os.Getenv("OTX_API_KEY")

	if abuseKey == "" {
		logWarning("ABUSEIPDB_API_KEY not set — AbuseIPDB enrichment will be skipped")
	}
	if otxKey == "" {
		logWarning("OTX_API_KEY not set — OTX enrichment will be skipped")
	}

	logInfo("Reading IP list from: %s", *inputFile)
	rawIOCs, err := readIPsFromFile(*inputFile)
	if err != nil {
		fatalError("Failed to read IP list: %v", err)
	}

	if len(rawIOCs) == 0 {
		fatalError("No IPs found in input file: %s", *inputFile)
	}

	// Deduplicate — consolidateIOCs() preserved AS-IS from original
	logInfo("Total IPs before deduplication: %d", len(rawIOCs))
	unique := consolidateIOCs(rawIOCs)
	logInfo("Total unique IPs after deduplication: %d", len(unique))

	// Load Tool 43's enriched corpus as a TTL cache. Read-only -- this
	// tool never writes to enriched_corpus.json (owned exclusively by
	// Tool 43 / enriched_corpus.yml). Runs 15 minutes AFTER this tool in
	// the real schedule (pipeline.yml at :00, enriched_corpus.yml at
	// :15), so on every run after the first, the corpus reflects the
	// PREVIOUS cycle's enrichment -- current-cycle IPs are always at
	// least one cycle "behind" the freshest corpus write, which is fine:
	// the TTL window is days, not hours, so a few hours of staleness in
	// the cache-check itself has no practical effect on correctness.
	corpus := make(map[string]CorpusEntry)
	if *corpusFile != "" {
		corpus = loadEnrichedCorpus(*corpusFile)
	}

	// Enrich concurrently
	logInfo("Enriching %d unique IP(s)...", len(unique))
	enriched := enrichAll(unique, abuseKey, otxKey, corpus)
	logInfo("Enrichment complete")

	// Write JSON output
	if err := writeEnrichedJSON(enriched, *outputFile); err != nil {
		fatalError("Failed to write output: %v", err)
	}

	logInfo("Threat IP report written to %s", *outputFile)
}

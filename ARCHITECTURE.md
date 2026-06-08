# THIR HA Architecture — Two-Node Oracle Cloud

## Overview
Two Oracle Cloud Always Free VM.Standard.E2.1.Micro instances connected via
Oracle VCN private networking.

## Nodes
| Node | Role | Private IP | Key Services |
|------|------|------------|--------------|
| VM1 | Sensor | 10.0.0.53 | Cowrie SSH :2222, Telnet :2323, cloudflared |
| VM2 | Brain | 10.0.0.73 | HAProxy, pipeline tools, rsync, cloudflared |

## Data flow

# OT Forensic Evidence Collection Checklist

Evidence collection guide for cyber incidents in operational technology environments. Addresses the unique challenges of OT forensics including proprietary systems, volatile data, and safety constraints.

## Critical Principles

1. **Safety first** — never compromise physical process safety for evidence collection
2. **Volatile first** — collect the most transient evidence before it's overwritten
3. **Chain of custody** — document who collected what, when, and how
4. **Minimize impact** — collection procedures should not disrupt operations unless absolutely necessary

## Volatile Evidence (Collect Immediately)

| Evidence | Source | Tool/Method | Notes |
|----------|--------|-------------|-------|
| Network traffic | Span port / tap on OT network | Wireshark, tcpdump, NetworkMiner | Capture at IT/OT boundary AND within OT segments |
| PLC memory | PLC via engineering workstation | Vendor-specific tools (Step 7, RSLogix) | Export current logic and compare to known-good |
| Running processes | Engineering workstations, HMI | Process Explorer, Volatility | Capture before any system changes |
| Active connections | Network devices, firewalls | netstat, conntrack, firewall session tables | Document all active sessions in/out of OT |
| Process historian data | Historian server | Historian export tools | Export last 72+ hours of process data |
| HMI screenshots | Operator consoles | Screenshots + HMI export | Document current displayed state |

## System Evidence (Collect Within Hours)

| Evidence | Source | Tool/Method | Notes |
|----------|--------|-------------|-------|
| Windows event logs | Engineering workstations, servers | wevtutil, Log Parser | Security, System, Application, PowerShell logs |
| Syslog | Linux-based OT devices | Remote syslog archive | May be limited on embedded devices |
| Authentication logs | AD, RADIUS, local accounts | Event log export, RADIUS logs | Focus on OT-connected accounts |
| Firewall logs | IT/OT boundary firewalls | Firewall management console | Connection logs, rule hit counts |
| IDS/IPS alerts | Security monitoring tools | SIEM export, IDS console | Alerts from OT-aware signatures |
| VPN/remote access logs | VPN concentrator | Admin console export | All remote access to OT network |

## Disk/Storage Evidence (Collect Within 24 Hours)

| Evidence | Source | Tool/Method | Notes |
|----------|--------|-------------|-------|
| Disk images | Compromised workstations | FTK Imager, dd | Full forensic image with hash verification |
| PLC project files | Engineering workstation | File copy with hashing | .S7P, .ACD, .RSS project files |
| Firmware images | PLCs, RTUs, switches | Vendor tools | Compare against known-good firmware hashes |
| Backup integrity | Backup systems | Backup verification tools | Verify backups are not also compromised |
| USB device history | Windows registry | RegRipper, Registry Explorer | USBSTOR entries for unauthorized devices |

## OT-Specific Considerations

### PLCs and RTUs
- Export current ladder logic / function block diagrams
- Compare against version-controlled baseline (if available)
- Document firmware version and last update timestamp
- Check for unauthorized program blocks or modifications to existing blocks

### SCADA / HMI Systems
- Export current display configurations
- Check for modified alarm thresholds or disabled alarms
- Review operator action logs
- Document any unauthorized user accounts

### Network Devices (OT switches, firewalls)
- Export running configuration
- Review MAC address tables for unknown devices
- Check for unauthorized routes or ACL modifications
- Capture spanning-tree topology

### Safety Instrumented Systems (SIS)
- Document SIS status WITHOUT modifying anything
- Any SIS evidence collection must be supervised by a process safety engineer
- Do not connect forensic tools directly to SIS networks
- If SIS compromise is suspected, escalate to vendor immediately

## Documentation Template

For each piece of evidence collected:

```
Evidence ID:        [unique identifier]
Description:        [what was collected]
Source system:      [hostname/IP/device]
Collection time:    [ISO 8601 timestamp]
Collected by:       [name and role]
Method:             [tool and procedure used]
Hash (SHA-256):     [hash of collected artifact]
Storage location:   [where the evidence is stored]
Chain of custody:   [who has handled it since collection]
Notes:              [any relevant observations]
```

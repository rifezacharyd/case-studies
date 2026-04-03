# Stuxnet - CVEs and Indicators of Compromise

## Zero-Day Vulnerabilities Exploited

| CVE | Description | Vector |
|-----|-------------|--------|
| **CVE-2010-2568** | Windows Shell LNK vulnerability | USB propagation — malicious .lnk files auto-executed when a USB drive was viewed in Explorer |
| **CVE-2010-2729** | Windows Print Spooler remote code execution | Network propagation across shared printers |
| **CVE-2010-2772** | Siemens SIMATIC WinCC hardcoded database password | Accessed WinCC SQL Server database using the default password |
| **CVE-2010-3338** | Windows Task Scheduler privilege escalation | Local privilege escalation to SYSTEM |
| **CVE-2010-3888** | Windows kernel vulnerability | Additional privilege escalation |

## Additional Propagation Methods

- **MS08-067** (CVE-2008-4250): Windows Server Service vulnerability (same as Conficker) — used for network propagation
- **Siemens Step 7 project file infection**: Hooked the Step 7 DLL to infect .S7P project files, spreading to any engineer who opened the project
- **Network shares**: Propagated across Windows network shares using stolen credentials
- **WinCC database connections**: Spread via SQL connections to WinCC database servers

## Digital Certificates (Stolen)

- **Realtek Semiconductor Corp.** — legitimate code signing certificate used to sign early Stuxnet drivers
- **JMicron Technology Corp.** — second legitimate certificate used after Realtek was revoked; both companies are located in the same business park in Hsinchu, Taiwan

## Key File Indicators

| Indicator | Value |
|-----------|-------|
| Primary DLL | `~WTR4141.tmp` (main payload loader) |
| Configuration block | 431 bytes of encoded configuration data within the main binary |
| Infection marker | Registry key `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\MS-DOS Emulation\NTVDM TRACE` set to `19790509` (a date referencing May 9, 1979) |
| C&C domains | `www.mypremierfutbol.com`, `www.todaysfutbol.com` |
| Target PLC model | Siemens S7-315 and S7-417 |
| Target frequency range | 807 Hz - 1210 Hz (centrifuge motor operating frequencies) |

## MITRE ATT&CK Techniques

Key techniques mapped to the ATT&CK framework:

- **T1091** - Replication Through Removable Media
- **T1203** - Exploitation for Client Execution
- **T1068** - Exploitation for Privilege Escalation
- **T1014** - Rootkit (both Windows and PLC-level rootkit)
- **T1027** - Obfuscated Files or Information
- **T1553.002** - Code Signing (stolen certificates)
- **T1071** - Application Layer Protocol (C&C via HTTP)
- **T0831** - Manipulation of Control (ICS-specific)
- **T0857** - System Firmware (PLC code injection)

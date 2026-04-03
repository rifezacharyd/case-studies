# Critical Infrastructure and the Cyber Threat Landscape

A survey of the threat landscape facing critical infrastructure sectors. Covers the sixteen sectors defined by PPD-21, nation-state threat actors, SCADA/ICS security challenges, and defensive frameworks.

## Key Findings

- PPD-21 designates 16 critical infrastructure sectors with deep interdependencies where compromise in one cascades to others
- Nation-state actors focus on persistent access (pre-positioning) rather than immediate exploitation
- OT security priorities are inverted from IT: Safety > Availability > Integrity > Confidentiality
- Legacy protocols (Modbus, DNP3) lack authentication and encryption by design

## Project Structure

```
critical-infrastructure-threats/
├── README.md
├── sectors.py               # Data model of all 16 CI sectors
├── threat_actors.md          # Nation-state threat actor profiles
├── frameworks_reference.md   # NIST CSF, SP 800-82, ISACs
└── purdue_model.py           # Purdue Model network visualization
```

## References

- Presidential Policy Directive 21 (PPD-21), 2013
- NIST Cybersecurity Framework (CSF) 2.0
- NIST SP 800-82 Rev. 3, Guide to OT Security
- CISA Critical Infrastructure Sector pages

---

*Part of a cybersecurity research portfolio. See the accompanying blog post for full analysis.*

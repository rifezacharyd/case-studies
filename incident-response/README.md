# Incident Response for Critical Infrastructure

An overview of incident response frameworks tailored to critical infrastructure environments. Covers the NIST incident response lifecycle, forensic preservation in OT environments, and coordination with government agencies.

## Key Findings

- Critical infrastructure IR requires balancing cybersecurity objectives against operational continuity and public safety
- The NIST SP 800-61r2 four-phase lifecycle is the foundation, but OT environments add unique constraints
- Pre-established relationships with CISA, FBI, and sector ISACs are critical before incidents occur
- OT forensics requires specialized approaches due to proprietary systems, volatile evidence, and safety constraints

## Project Structure

```
incident-response/
├── README.md
├── ir_lifecycle.py           # NIST IR lifecycle data model with OT checklists
├── agency_coordination.md    # Government agency coordination guide
├── playbook_template.yaml    # ICS-specific IR playbook template
└── evidence_checklist.md     # OT forensic evidence collection checklist
```

## References

- NIST SP 800-61r2: Computer Security Incident Handling Guide
- NIST SP 800-82 Rev. 3: Guide to OT Security
- CISA Incident Reporting: cisa.gov/report
- CIRCIA: Cyber Incident Reporting for Critical Infrastructure Act of 2022

---

*Part of a cybersecurity research portfolio. See the accompanying blog post for full analysis.*

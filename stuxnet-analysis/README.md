# Stuxnet and the Rise of Cyber Weapons

An examination of Stuxnet, the first known cyber weapon deployed against critical infrastructure. Explores how this malware changed the landscape of national security, industrial control system vulnerabilities, and the doctrine of cyber warfare.

## Key Findings

- Stuxnet was the first malware designed to cause physical destruction, targeting uranium enrichment centrifuges at Iran's Natanz facility
- The malware exploited four zero-day vulnerabilities and used stolen digital certificates, indicating nation-state resources
- It crossed air-gapped networks via USB drives and included safeguards to limit collateral damage
- Stuxnet exposed fundamental vulnerabilities in ICS/SCADA systems never designed for cybersecurity

## Project Structure

```
stuxnet-analysis/
├── README.md
├── timeline.md            # Chronological discovery and attribution timeline
├── ioc_references.md      # CVEs and indicators of compromise
└── attack_flow.py         # Educational attack chain visualization
```

## References

- Langner, Ralph. "To Kill a Centrifuge." The Langner Group, 2013.
- Zetter, Kim. "Countdown to Zero Day." Crown, 2014.
- Symantec. "W32.Stuxnet Dossier." Version 1.4, 2011.
- CISA ICS-CERT advisories on Siemens SIMATIC vulnerabilities

---

*Part of a cybersecurity research portfolio. See the accompanying blog post for full analysis.*

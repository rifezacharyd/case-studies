# Supply Chain Attacks and National Security

Analyzing major supply chain compromises including SolarWinds, Log4j, NotPetya, and XZ Utils. Examines their impact on national security and the frameworks being developed to secure the software supply chain.

## Key Findings

- Supply chain attacks exploit trust relationships to compromise thousands of downstream targets through a single vendor
- Two primary patterns: deliberate build pipeline compromise (SolarWinds) and exploitation of open-source vulnerabilities (Log4j)
- Software Bill of Materials (SBOM) and provenance verification are emerging as essential defenses
- Executive Order 14028 mandates new supply chain security requirements for federal agencies

## Project Structure

```
supply-chain-attacks/
├── README.md
├── incidents/
│   ├── solarwinds.md       # SolarWinds/SUNBURST analysis
│   ├── log4j.md            # Log4j/CVE-2021-44228
│   ├── notpetya.md         # NotPetya via M.E.Doc
│   ├── kaseya.md           # Kaseya VSA ransomware
│   ├── 3cx.md              # 3CX chained supply chain attack
│   └── xz_utils.md         # XZ Utils backdoor attempt
├── sbom_checker.py          # Dependency vulnerability checker
└── frameworks.md            # SLSA, OpenSSF, Sigstore reference
```

## References

- CISA Supply Chain Risk Management guidance
- Executive Order 14028 on Improving the Nation's Cybersecurity
- SLSA (Supply-chain Levels for Software Artifacts) specification
- OpenSSF Scorecard project

---

*Part of a cybersecurity research portfolio. See the accompanying blog post for full analysis.*

# Government Agency Coordination Guide

Reference for which government agencies to contact during a critical infrastructure cyber incident, when to contact them, and what to expect.

## Primary Contacts

### CISA (Cybersecurity and Infrastructure Security Agency)

- **Role**: Lead federal agency for critical infrastructure cybersecurity; provides technical assistance, threat intelligence, and incident coordination
- **When to contact**: Any suspected or confirmed cyber incident affecting critical infrastructure
- **How**: cisa.gov/report or 888-282-0870 (24/7)
- **What they provide**: Free on-site incident response support, malware analysis, threat intelligence, vulnerability scanning
- **Reporting requirement**: Mandatory for covered entities under CIRCIA (72 hours for incidents, 24 hours for ransomware payments)

### FBI (Federal Bureau of Investigation)

- **Role**: Criminal investigation and counterintelligence
- **When to contact**: When criminal activity is suspected (ransomware, data theft, insider threat) or when nation-state attribution is relevant
- **How**: Contact local FBI field office or ic3.gov for cyber complaints
- **What they provide**: Criminal investigation, potential for asset recovery (especially ransomware payments), counterintelligence context
- **Note**: FBI investigation is separate from CISA technical assistance — contact both

### NSA / CNMF (Cyber National Mission Force)

- **Role**: Signals intelligence, technical threat intelligence, hunt-forward operations
- **When to contact**: Typically engaged through CISA or DoD channels, not directly by private sector
- **What they provide**: Deep technical intelligence on nation-state TTPs, defensive recommendations based on classified intelligence

## Sector-Specific Contacts

### Information Sharing and Analysis Centers (ISACs)

Contact your sector's ISAC for peer threat intelligence and sector-specific guidance:

| Sector | ISAC | Contact |
|--------|------|---------|
| Electricity | E-ISAC | electricityisac.com |
| Water | WaterISAC | waterisac.org |
| Financial | FS-ISAC | fsisac.com |
| Healthcare | H-ISAC | h-isac.org |
| IT | IT-ISAC | it-isac.org |
| Oil & Gas | ONG-ISAC | ongisac.org |

### State/Local Fusion Centers

- Regional threat coordination and local law enforcement interface
- Find your fusion center: dhs.gov/fusion-centers

## Coordination Timeline

| Timeframe | Action |
|-----------|--------|
| **0-1 hours** | Activate internal IR team; begin detection and analysis |
| **1-4 hours** | If CI impact confirmed: notify CISA (888-282-0870) and sector ISAC |
| **4-24 hours** | Contact FBI field office if criminal activity suspected; engage legal counsel on reporting obligations |
| **24-72 hours** | Submit formal CIRCIA report if applicable; share IOCs with ISAC partners |
| **Ongoing** | Coordinate with CISA for technical assistance; support FBI investigation if applicable |

## Legal Considerations

- Involve legal counsel early to assess reporting obligations and liability protections
- CIRCIA provides limited liability protections for organizations that report in good faith
- Attorney-client privilege considerations for forensic reports vs. business records
- Regulatory notification requirements vary by sector (HIPAA for healthcare, SOX for financial, etc.)
- Cyber insurance carrier notification deadlines — check policy for specific requirements

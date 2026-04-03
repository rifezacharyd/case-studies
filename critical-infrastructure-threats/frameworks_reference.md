# Defensive Frameworks Reference

## NIST Cybersecurity Framework (CSF) 2.0

The primary framework for organizing cybersecurity activities across critical infrastructure.

### Six Core Functions

| Function | Purpose |
|----------|---------|
| **Govern** | Establish and monitor cybersecurity risk management strategy, expectations, and policy (new in CSF 2.0) |
| **Identify** | Understand organizational context, assets, risks, and supply chain |
| **Protect** | Implement safeguards to ensure delivery of critical services |
| **Detect** | Identify cybersecurity events in a timely manner |
| **Respond** | Take action regarding detected cybersecurity incidents |
| **Recover** | Restore capabilities impaired by cybersecurity incidents |

## NIST SP 800-82 Rev. 3 — Guide to OT Security

Specific guidance for securing industrial control systems and operational technology environments.

### Key Recommendations

- Establish a clear boundary between IT and OT networks using demilitarized zones (DMZ)
- Apply the principle of least privilege to all ICS access
- Implement defense-in-depth with multiple layers of security controls
- Develop and regularly test ICS-specific incident response plans
- Monitor OT network traffic for anomalous behavior
- Maintain an accurate inventory of all OT assets including firmware versions

### The Purdue Model

SP 800-82 references the Purdue Enterprise Reference Architecture for network segmentation:

- **Level 0**: Physical process (sensors, actuators)
- **Level 1**: Basic control (PLCs, RTUs)
- **Level 2**: Area supervisory control (HMI, SCADA)
- **Level 3**: Site operations (historian, engineering workstations)
- **DMZ**: Demilitarized zone between OT and IT
- **Level 4**: Enterprise IT (email, ERP, business systems)
- **Level 5**: Enterprise network / internet

## Sector-Specific ISACs

Information Sharing and Analysis Centers facilitate threat intelligence sharing within each sector.

| ISAC | Sector | Website |
|------|--------|---------|
| E-ISAC | Electricity | electricityisac.com |
| WaterISAC | Water/Wastewater | waterisac.org |
| FS-ISAC | Financial Services | fsisac.com |
| H-ISAC | Healthcare | h-isac.org |
| IT-ISAC | Information Technology | it-isac.org |
| ONG-ISAC | Oil & Natural Gas | ongisac.org |
| A-ISAC | Aviation | a-isac.com |
| MS-ISAC | State/Local Government | cisecurity.org/ms-isac |

## MITRE ATT&CK for ICS

A knowledge base of adversary tactics and techniques specific to industrial control systems. Extends the enterprise ATT&CK framework with ICS-specific techniques.

Key tactic categories: Initial Access, Execution, Persistence, Evasion, Discovery, Lateral Movement, Collection, Command and Control, Inhibit Response Function, Impair Process Control, Impact.

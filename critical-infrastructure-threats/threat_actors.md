# Nation-State Threat Actor Profiles

Profiles of major threat actor groups known to target critical infrastructure, based on publicly attributed campaigns and government advisories.

## Volt Typhoon (PRC)

- **Attribution**: People's Republic of China
- **Active**: 2021 - present
- **Targets**: U.S. critical infrastructure (communications, energy, transportation, water)
- **TTPs**: Living-off-the-land techniques using built-in Windows tools (cmd, PowerShell, wmic, ntdsutil); avoids custom malware to evade detection; exploits internet-facing appliances (Fortinet, Ivanti, SOHO routers) for initial access
- **Objective**: Pre-positioning for potential disruption during geopolitical conflict
- **Key Advisory**: CISA AA24-038A (Feb 2024)

## Sandworm (GRU, Russia)

- **Attribution**: Russian GRU Unit 74455
- **Active**: 2014 - present
- **Targets**: Ukraine power grid, global IT infrastructure, Olympic Games
- **TTPs**: Custom ICS malware (Industroyer/CrashOverride, Industroyer2), destructive wipers (NotPetya, WhisperGate), supply chain compromise (M.E.Doc)
- **Notable Incidents**:
  - 2015: Ukraine power grid attack (BlackEnergy + KillDisk) — first confirmed cyber-caused power outage
  - 2016: Industroyer attack on Ukraine's Pivnichna substation
  - 2017: NotPetya — $10B+ global damage via compromised M.E.Doc update
  - 2022: Industroyer2 targeting Ukraine grid during Russian invasion
- **Key Advisory**: CISA AA22-110A

## TRITON / XENOTIME

- **Attribution**: Linked to a Russian government research institution (CNIIHM)
- **Active**: 2017 - present
- **Targets**: Safety Instrumented Systems (SIS) in petrochemical facilities
- **TTPs**: Targeted Triconex SIS controllers with custom framework (TRITON/TRISIS) designed to disable safety systems — the last automated defense against catastrophic physical failure
- **Significance**: First known malware designed to target industrial safety systems
- **Key Advisory**: CISA MAR-17-352-01

## APT33 / Elfin (Iran)

- **Attribution**: Iran (MOIS/IRGC)
- **Active**: 2013 - present
- **Targets**: Aviation, energy, and petrochemical sectors (Saudi Arabia, U.S., South Korea)
- **TTPs**: Spear-phishing, credential harvesting, destructive wipers (Shamoon lineage), targeting of ICS vendors and integrators for supply chain access
- **Objective**: Espionage and retaliatory destructive capability

## Lazarus Group (DPRK)

- **Attribution**: North Korea (RGB)
- **Active**: 2009 - present
- **Targets**: Financial institutions, cryptocurrency exchanges, critical infrastructure
- **TTPs**: Custom malware, social engineering, supply chain attacks (3CX), cryptocurrency theft for regime funding
- **Notable Incidents**: Sony Pictures (2014), Bangladesh Bank SWIFT attack (2016), WannaCry (2017), 3CX supply chain (2023)

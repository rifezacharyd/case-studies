# NotPetya (2017)

## Overview

Destructive malware disguised as ransomware, distributed through a compromised update to M.E.Doc, a Ukrainian accounting software used by most businesses operating in Ukraine. Caused over $10 billion in global damage.

## Timeline

- **Jun 27, 2017**: M.E.Doc pushes compromised update; NotPetya begins spreading
- **Jun 27-28, 2017**: Global organizations report mass system outages — Maersk, Merck, FedEx/TNT Express, Mondelez, Reckitt Benckiser
- **Jul 2017**: Attribution to Russian GRU (Sandworm/Unit 74455)
- **Feb 2018**: U.S., UK, Australia, and other governments formally attribute NotPetya to Russia

## Technical Details

- **Distribution**: Hijacked M.E.Doc update mechanism (legitimate auto-update pushed backdoored code)
- **Propagation**: EternalBlue (MS17-010) and EternalRomance exploits, Mimikatz-style credential harvesting, WMI and PsExec lateral movement
- **Payload**: Overwrote MBR and encrypted MFT; despite displaying a ransom note, the encryption was irreversible by design — no decryption key existed
- **Destructive intent**: The inability to decrypt confirmed this was a destructive wiper, not ransomware

## Impact

- Maersk: 49,000 laptops, 3,500 servers destroyed; 10 days to rebuild entire infrastructure
- Merck: $870M in damages
- FedEx/TNT Express: $400M in damages
- Total global damage estimated at $10B+
- Largest destructive cyberattack in history at time of occurrence

## Lessons

- Supply chain compromise can achieve global reach through a single regional software vendor
- Destructive malware can masquerade as ransomware
- Business continuity planning must account for total infrastructure loss

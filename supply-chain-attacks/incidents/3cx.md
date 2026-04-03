# 3CX Supply Chain Attack (2023)

## Overview

A supply chain attack on 3CX, a VoIP/PBX provider with 600,000+ customers, notable for being the first publicly documented case of one supply chain attack leading directly to another.

## Timeline

- **2021-2022**: An employee at 3CX installs a trojanized version of X_TRADER, a financial trading application from Trading Technologies (itself a supply chain compromise)
- **Jan-Mar 2023**: Adversary uses access from X_TRADER compromise to move laterally within 3CX's network and compromise the build environment
- **Mar 29, 2023**: CrowdStrike and SentinelOne detect malicious activity in 3CX Desktop App
- **Mar 30, 2023**: 3CX CEO confirms compromise; CISA issues advisory

## Technical Details

- **Chain**: Trading Technologies X_TRADER compromise → 3CX employee workstation → 3CX build environment → 3CX Desktop App (macOS and Windows) → end users
- **Payload**: Trojanized 3CX app loaded malicious DLLs that retrieved encrypted C2 data from GitHub icon files
- **Attribution**: Attributed to Lazarus Group (DPRK)

## Impact

- 600,000+ organizations use 3CX
- Demonstrated that supply chain attacks can cascade (supply chain of supply chains)
- Highlighted risk from developer workstation compromise

## Lessons

- Developer environments are high-value targets for supply chain adversaries
- Supply chain attacks can chain through multiple vendors
- Even "trusted" applications on developer machines can be compromised entry points

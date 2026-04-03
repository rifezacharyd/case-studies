# SolarWinds / SUNBURST (2020)

## Overview

A nation-state adversary compromised the SolarWinds Orion build pipeline, inserting a backdoor (SUNBURST) into legitimate, digitally signed software updates distributed to approximately 18,000 organizations.

## Timeline

- **Mar 2020**: Trojanized Orion updates begin distribution (versions 2019.4 HF 5 through 2020.2.1)
- **Dec 8, 2020**: FireEye discloses it was breached and its red team tools were stolen
- **Dec 13, 2020**: FireEye attributes its breach to a compromised SolarWinds update; CISA issues Emergency Directive 21-01
- **Dec 2020 - Jan 2021**: Scope of compromise revealed — U.S. Treasury, Commerce, DHS, DOE, and multiple Fortune 500 companies

## Technical Details

- **Initial compromise**: Adversary gained access to SolarWinds build environment
- **Implant**: SUNBURST backdoor injected into `SolarWinds.Orion.Core.BusinessLayer.dll`
- **C2**: DNS-based command and control using subdomains of `avsvmcloud.com`, designed to mimic legitimate SolarWinds API traffic
- **Stealth**: 12-14 day dormancy period before activating; checked for security tools and sandbox environments; blended C2 traffic with normal Orion telemetry
- **Second-stage**: TEARDROP memory-only dropper deployed to high-value targets for Cobalt Strike beacon delivery

## Impact

- ~18,000 organizations installed the trojanized update
- ~100 organizations selected for deeper exploitation
- 9+ federal agencies confirmed compromised
- Estimated remediation cost exceeds $100M for SolarWinds alone

## Lessons

- Build pipeline integrity is a critical security requirement
- Code signing alone is insufficient if the build process is compromised
- Supply chain monitoring must include behavioral analysis of trusted software

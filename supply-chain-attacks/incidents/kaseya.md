# Kaseya VSA (2021)

## Overview

The REvil ransomware group exploited vulnerabilities in Kaseya VSA, a remote monitoring and management platform used by managed service providers (MSPs), to deploy ransomware to hundreds of downstream businesses.

## Timeline

- **Jul 2, 2021**: REvil exploits Kaseya VSA zero-days during U.S. Independence Day weekend
- **Jul 2-5, 2021**: ~60 MSPs compromised, affecting 800-1,500 downstream businesses
- **Jul 5, 2021**: REvil demands $70M universal decryptor ransom
- **Jul 13, 2021**: REvil infrastructure goes offline
- **Jul 22, 2021**: Kaseya obtains universal decryptor key (source undisclosed)

## Technical Details

- **Vulnerabilities**: Authentication bypass and SQL injection in Kaseya VSA on-premises servers (CVE-2021-30116)
- **Attack path**: Exploited VSA servers → pushed malicious "agent update" to all managed endpoints → REvil ransomware deployment
- **Leverage**: MSP model meant a single VSA compromise could reach hundreds of end customers

## Impact

- 60+ MSPs compromised
- 800-1,500 downstream businesses affected
- Swedish grocery chain Coop forced to close 800 stores
- Demonstrated how MSP platforms create one-to-many attack opportunities

## Lessons

- MSP/RMM platforms represent high-value supply chain targets
- Zero-day vulnerabilities in management tools have outsized blast radius
- Weekend/holiday timing is a deliberate adversary strategy

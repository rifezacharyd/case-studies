# XZ Utils Backdoor (2024)

## Overview

A multi-year social engineering campaign to insert a backdoor into XZ Utils (liblzma), a critical compression library used by nearly every Linux distribution. The backdoor was discovered just before reaching widespread stable distribution channels.

## Timeline

- **2021**: "Jia Tan" begins contributing to XZ Utils project
- **2022**: Sockpuppet accounts pressure the sole maintainer to add Jia Tan as a co-maintainer
- **2023**: Jia Tan gains commit and release authority
- **Feb 2024**: Backdoor code inserted across multiple commits in versions 5.6.0 and 5.6.1
- **Mar 29, 2024**: Andres Freund (Microsoft/PostgreSQL developer) discovers the backdoor while investigating SSH performance anomalies — 500ms latency increase during login
- **Mar 29, 2024**: CVE-2024-3094 assigned with CVSS 10.0

## Technical Details

- **Target**: sshd (OpenSSH server) via systemd's dependency on liblzma
- **Mechanism**: Malicious build scripts injected obfuscated object code during the build process; the backdoor hooked into RSA signature verification in sshd, allowing unauthorized remote access
- **Stealth**: Backdoor code was hidden in test fixture binary files (.xz format), making it invisible to casual code review; malicious build logic was split across multiple commits
- **Trigger**: The backdoor only activated when sshd was invoked by systemd, specifically on x86_64 Linux with glibc and specific build flags

## Impact

- Caught before reaching most stable Linux distributions
- Fedora 40 beta and Fedora Rawhide were briefly affected
- Debian testing/unstable had the vulnerable version temporarily
- Highlighted the fragility of open-source projects maintained by single individuals

## Lessons

- Social engineering of open-source maintainers is a viable nation-state attack vector
- Single-maintainer projects supporting critical infrastructure represent systemic risk
- Build reproducibility and binary transparency could have detected the discrepancy between source and build output
- Performance anomaly detection (not security tooling) caught this backdoor

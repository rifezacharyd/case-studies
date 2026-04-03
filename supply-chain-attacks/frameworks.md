# Supply Chain Security Frameworks

## SLSA (Supply-chain Levels for Software Artifacts)

A framework for ensuring the integrity of software artifacts throughout the supply chain, created by Google.

### Levels

| Level | Requirements |
|-------|-------------|
| **SLSA 1** | Build process is documented and generates provenance |
| **SLSA 2** | Build is run on a hosted build service; provenance is signed |
| **SLSA 3** | Hardened build platform with tamper-proof provenance; source is version-controlled and reviewed |

### Core Principles
- Every step from source to distribution should be auditable
- Build provenance should be automatically generated and verifiable
- Dependencies should be complete and accurate

## OpenSSF Scorecard

An automated tool that assesses the security practices of open-source projects. Checks include:

- **Branch protection**: Are the default and release branches protected?
- **Code review**: Are changes reviewed before merging?
- **CI tests**: Does the project run tests in CI?
- **Dependency updates**: Are dependencies kept up to date?
- **Fuzzing**: Is the project fuzzed?
- **License**: Does the project have a license?
- **Maintained**: Is the project actively maintained?
- **Signed releases**: Are releases signed?
- **Vulnerabilities**: Are there unfixed vulnerabilities?
- **SAST**: Is static analysis used?

Usage: `scorecard --repo=github.com/org/repo`

## Sigstore

A project providing free code signing and verification for open-source software.

### Components

- **Cosign**: Container and artifact signing
- **Fulcio**: Certificate authority that issues short-lived certificates based on OIDC identity
- **Rekor**: Transparency log for signatures and attestations

### Key Benefit
Eliminates the need for developers to manage long-lived signing keys — the primary barrier to adoption of software signing.

## CISA SBOM Initiatives

CISA promotes Software Bill of Materials (SBOM) as a foundational element of supply chain security.

### Minimum SBOM Elements (NTIA)
- Supplier name
- Component name
- Version
- Unique identifier
- Dependency relationship
- Author of SBOM data
- Timestamp

### Supported Formats
- **SPDX** (Linux Foundation) — ISO/IEC 5962:2021
- **CycloneDX** (OWASP) — focused on security use cases
- **SWID Tags** (ISO/IEC 19770-2) — software identification

## Executive Order 14028

Signed May 12, 2021, establishing new cybersecurity requirements for federal agencies and their software suppliers.

### Key Requirements
- SBOM required for software sold to federal government
- Secure software development practices (NIST SSDF)
- Enhanced logging and detection requirements
- Zero-trust architecture adoption
- Incident reporting timelines

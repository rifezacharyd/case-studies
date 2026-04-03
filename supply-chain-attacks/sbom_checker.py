"""
SBOM Dependency Vulnerability Checker

Reads a Python requirements.txt and checks packages against a
reference database of known vulnerable versions. Demonstrates
the concept behind Software Bill of Materials analysis.

Note: This uses a built-in reference database for demonstration.
In production, use tools like pip-audit, safety, or OSV.dev API.
"""

import sys
import re
from pathlib import Path


# Simulated vulnerability database (real-world: use OSV.dev, NVD, or safety-db)
VULN_DB = {
    "requests": [
        {"affected": "<2.31.0", "cve": "CVE-2023-32681", "severity": "MEDIUM",
         "description": "Unintended leak of Proxy-Authorization header"},
    ],
    "urllib3": [
        {"affected": "<2.0.7", "cve": "CVE-2023-45803", "severity": "MEDIUM",
         "description": "Request body not stripped on redirect"},
    ],
    "cryptography": [
        {"affected": "<41.0.6", "cve": "CVE-2023-49083", "severity": "HIGH",
         "description": "NULL pointer dereference in PKCS7 processing"},
    ],
    "pillow": [
        {"affected": "<10.2.0", "cve": "CVE-2023-50447", "severity": "HIGH",
         "description": "Arbitrary code execution via crafted image"},
    ],
    "django": [
        {"affected": "<4.2.8", "cve": "CVE-2023-46695", "severity": "HIGH",
         "description": "Denial of service via large file upload"},
    ],
    "flask": [
        {"affected": "<2.3.2", "cve": "CVE-2023-30861", "severity": "HIGH",
         "description": "Session cookie sent over non-HTTPS"},
    ],
    "paramiko": [
        {"affected": "<3.4.0", "cve": "CVE-2023-48795", "severity": "MEDIUM",
         "description": "Terrapin attack - SSH prefix truncation"},
    ],
    "jinja2": [
        {"affected": "<3.1.3", "cve": "CVE-2024-22195", "severity": "MEDIUM",
         "description": "Cross-site scripting via xmlattr filter"},
    ],
}


def parse_requirements(filepath: str) -> list[tuple[str, str]]:
    """Parse a requirements.txt and return list of (package, version_spec)."""
    packages = []
    path = Path(filepath)

    if not path.exists():
        print(f"[!] File not found: {filepath}")
        return packages

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue

            # Parse package>=version, package==version, etc.
            match = re.match(r"^([a-zA-Z0-9_-]+)\s*([><=!~]+)?\s*([0-9.]*)", line)
            if match:
                name = match.group(1).lower().replace("-", "_").replace("_", "-")
                version = match.group(3) or "unknown"
                packages.append((name, version))

    return packages


def check_vulnerabilities(packages: list[tuple[str, str]]) -> list[dict]:
    """Check packages against the vulnerability database."""
    findings = []

    for pkg_name, pkg_version in packages:
        # Normalize name for lookup
        normalized = pkg_name.lower().replace("-", "").replace("_", "")

        for db_name, vulns in VULN_DB.items():
            db_normalized = db_name.lower().replace("-", "").replace("_", "")
            if normalized == db_normalized:
                for vuln in vulns:
                    findings.append({
                        "package": pkg_name,
                        "installed_version": pkg_version,
                        "affected_range": vuln["affected"],
                        "cve": vuln["cve"],
                        "severity": vuln["severity"],
                        "description": vuln["description"],
                    })

    return findings


def generate_report(filepath: str):
    """Analyze a requirements.txt and print a vulnerability report."""
    print("=" * 65)
    print("  SBOM DEPENDENCY VULNERABILITY CHECK")
    print("=" * 65)
    print(f"  Source: {filepath}")
    print()

    packages = parse_requirements(filepath)

    if not packages:
        print("  No packages found.")
        return

    print(f"  Packages found: {len(packages)}")
    for name, version in packages:
        print(f"    {name} {version}")

    print(f"\n{'─' * 65}")
    print("  VULNERABILITY CHECK (reference database)")
    print(f"{'─' * 65}\n")

    findings = check_vulnerabilities(packages)

    if not findings:
        print("  [+] No known vulnerabilities found in reference database.")
    else:
        print(f"  [{len(findings)} potential finding(s)]\n")
        for f in findings:
            severity_icon = {"HIGH": "!!!", "MEDIUM": "!!", "LOW": "!"}.get(f["severity"], "?")
            print(f"  [{severity_icon}] {f['cve']} ({f['severity']})")
            print(f"      Package: {f['package']} (installed: {f['installed_version']})")
            print(f"      Affected: {f['affected_range']}")
            print(f"      {f['description']}")
            print()

    print(f"{'─' * 65}")
    print("  NOTE: This is a demonstration tool with a limited reference")
    print("  database. For production use, see: pip-audit, safety, OSV.dev")
    print(f"{'─' * 65}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <requirements.txt>")
        sys.exit(1)

    generate_report(sys.argv[1])

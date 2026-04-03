"""
Stuxnet Attack Chain Visualization

Educational tool that models and displays the Stuxnet attack chain
as an ASCII diagram. This is NOT malware — it is a data structure
representing the publicly documented kill chain for study purposes.
"""


ATTACK_PHASES = [
    {
        "phase": "1. Initial Access",
        "technique": "USB Drive Infection",
        "detail": "Malicious .lnk files exploit CVE-2010-2568 to auto-execute when removable media is viewed in Windows Explorer",
        "target": "Windows workstations connected to the target facility network",
    },
    {
        "phase": "2. Propagation",
        "technique": "Multi-Vector Spreading",
        "detail": "Network shares (MS08-067), print spooler (CVE-2010-2729), Step 7 project files, WinCC database connections",
        "target": "All reachable Windows systems within the facility network",
    },
    {
        "phase": "3. Privilege Escalation",
        "technique": "Kernel Exploits + Stolen Certificates",
        "detail": "CVE-2010-3338 (Task Scheduler) and CVE-2010-3888 for SYSTEM access; signed drivers using stolen Realtek/JMicron certificates",
        "target": "Local system privileges on infected hosts",
    },
    {
        "phase": "4. Discovery & Targeting",
        "technique": "Environment Fingerprinting",
        "detail": "Checks for Siemens Step 7 / WinCC software, specific PLC models (S7-315/S7-417), and frequency converter configurations matching Natanz centrifuge specs",
        "target": "Only activates payload on systems matching exact target profile",
    },
    {
        "phase": "5. Lateral Movement to OT",
        "technique": "Step 7 Project Infection",
        "detail": "Hooks Siemens Step 7 DLL (s7otbxdx.dll) to intercept communications between engineering workstation and PLCs",
        "target": "Bridge from IT network to OT/ICS environment",
    },
    {
        "phase": "6. PLC Code Injection",
        "technique": "Man-in-the-Middle on PLC Communications",
        "detail": "Replaces legitimate PLC code blocks (OB1, OB35) with malicious versions while returning normal data to monitoring systems",
        "target": "Siemens S7-300 PLCs controlling variable-frequency drives",
    },
    {
        "phase": "7. Physical Destruction",
        "technique": "Centrifuge Speed Manipulation",
        "detail": "Periodically drives centrifuge motors to 1410 Hz (above design limit) then drops to 2 Hz, causing mechanical stress and bearing failure",
        "target": "IR-1 uranium enrichment centrifuges at Natanz",
    },
    {
        "phase": "8. Concealment",
        "technique": "Dual Rootkit (Windows + PLC)",
        "detail": "Windows rootkit hides malicious files; PLC rootkit replays recorded 'normal' process data to SCADA displays while attack executes",
        "target": "Operators see normal readings; damage accumulates undetected",
    },
]


def render_attack_chain():
    """Render the full Stuxnet attack chain as ASCII art."""
    width = 72

    print("=" * width)
    print("  STUXNET ATTACK CHAIN — EDUCATIONAL REFERENCE".center(width))
    print("=" * width)
    print()

    for i, phase in enumerate(ATTACK_PHASES):
        # Phase header
        print(f"  ┌{'─' * (width - 4)}┐")
        print(f"  │ {phase['phase']:<{width - 5}}│")
        print(f"  ├{'─' * (width - 4)}┤")

        # Technique
        print(f"  │ Technique: {phase['technique']:<{width - 16}}│")

        # Detail (word-wrap)
        detail = phase["detail"]
        max_line = width - 16
        words = detail.split()
        lines = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 <= max_line:
                current = f"{current} {word}" if current else word
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)

        print(f"  │ Detail:    {lines[0]:<{max_line}}│")
        for line in lines[1:]:
            print(f"  │            {line:<{max_line}}│")

        # Target
        target = phase["target"]
        t_lines = []
        current = ""
        for word in target.split():
            if len(current) + len(word) + 1 <= max_line:
                current = f"{current} {word}" if current else word
            else:
                t_lines.append(current)
                current = word
        if current:
            t_lines.append(current)

        print(f"  │ Target:    {t_lines[0]:<{max_line}}│")
        for line in t_lines[1:]:
            print(f"  │            {line:<{max_line}}│")

        print(f"  └{'─' * (width - 4)}┘")

        # Arrow between phases
        if i < len(ATTACK_PHASES) - 1:
            print(f"{'│':>{width // 2}}")
            print(f"{'▼':>{width // 2}}")

    print()
    print("=" * width)
    print("  Source: Symantec W32.Stuxnet Dossier, Langner 2013".center(width))
    print("=" * width)


if __name__ == "__main__":
    render_attack_chain()

"""
NIST Incident Response Lifecycle Model

Data model of the NIST SP 800-61r2 four-phase IR lifecycle
with checklists tailored for critical infrastructure and
OT/ICS environments.
"""


IR_LIFECYCLE = {
    "phase_1_preparation": {
        "name": "Preparation",
        "objective": "Establish and maintain IR capability before incidents occur",
        "checklist": [
            "Maintain current asset inventory including all OT/ICS devices, firmware versions, and network maps",
            "Establish IR team with cross-functional representation (IT security, OT engineering, legal, comms, executive)",
            "Develop and distribute IR playbooks for sector-specific scenarios",
            "Set up out-of-band communication channels (satellite phone, encrypted messaging) for use when primary networks are compromised",
            "Pre-establish relationships with CISA regional team, FBI field office, and sector ISAC",
            "Maintain forensic toolkit with tools compatible with OT systems (PLC imaging, historian export, network capture)",
            "Conduct tabletop exercises at least quarterly with scenarios involving OT compromise",
            "Verify backup and recovery procedures for both IT and OT systems",
            "Define escalation criteria — what constitutes an OT-impacting incident vs. IT-only",
            "Maintain vendor contact list for all ICS equipment with emergency support agreements",
        ],
    },
    "phase_2_detection_analysis": {
        "name": "Detection and Analysis",
        "objective": "Identify that an incident has occurred, determine scope, and assess impact",
        "checklist": [
            "Monitor IT network indicators: IDS/IPS alerts, SIEM correlation, endpoint detection",
            "Monitor OT-specific indicators: anomalous process values, unexpected PLC logic changes, unusual HMI commands",
            "Check for physical process anomalies: pressure, temperature, flow rate, or motor speed deviations",
            "Correlate IT and OT indicators — lateral movement from IT to OT is a critical escalation",
            "Determine if adversary has reached Level 2 or below in the Purdue Model",
            "Assess potential physical safety impact of the compromise",
            "Document all findings with timestamps in the incident log",
            "Classify incident severity using organization's defined scale",
            "Notify IR team leads and initiate communication protocols",
            "Begin evidence preservation procedures (see evidence_checklist.md)",
        ],
    },
    "phase_3_containment_eradication_recovery": {
        "name": "Containment, Eradication, and Recovery",
        "objective": "Stop the spread, remove the adversary, and restore operations",
        "containment_checklist": [
            "Evaluate containment options against operational impact — isolating a system may disrupt critical services",
            "Implement network segmentation to isolate compromised zones without disrupting safety systems",
            "Block identified C2 channels at network boundaries",
            "Disable compromised accounts and rotate credentials for IT and OT systems",
            "If OT compromise confirmed: consult with process engineers before any containment action",
            "NEVER power off safety instrumented systems (SIS) as a containment measure",
        ],
        "eradication_checklist": [
            "Identify all compromised systems across IT and OT environments",
            "Remove adversary persistence mechanisms (scheduled tasks, modified firmware, implanted code)",
            "Verify PLC/RTU logic against known-good backups",
            "Re-image compromised IT systems from clean media",
            "Patch exploited vulnerabilities where operationally feasible",
        ],
        "recovery_checklist": [
            "Restore systems from verified clean backups, starting with most critical services",
            "Validate OT system operation in a staged manner — do not bring all processes online simultaneously",
            "Monitor restored systems closely for signs of re-compromise",
            "Verify physical process operation matches expected parameters",
            "Conduct validation testing before returning systems to full production",
        ],
    },
    "phase_4_post_incident": {
        "name": "Post-Incident Activity",
        "objective": "Document lessons learned and improve defenses",
        "checklist": [
            "Conduct lessons-learned meeting within 1-2 weeks with all stakeholders",
            "Document complete incident timeline from initial access to resolution",
            "Identify gaps in detection, containment, and recovery capabilities",
            "Update IR playbooks based on lessons learned",
            "Share relevant threat intelligence with sector ISAC (anonymized if needed)",
            "Report to CISA as required under CIRCIA or voluntarily for community benefit",
            "Update asset inventory and network maps to reflect any changes made during response",
            "Implement defensive improvements identified during the incident",
            "Brief executive leadership on findings, impact, and recommended investments",
            "Schedule follow-up review to verify improvements were implemented",
        ],
    },
}


def display_lifecycle():
    """Display the full IR lifecycle with checklists."""
    print("=" * 65)
    print("  NIST INCIDENT RESPONSE LIFECYCLE (Critical Infrastructure)")
    print("  Based on SP 800-61r2 with OT/ICS extensions")
    print("=" * 65)

    for phase_key, phase in IR_LIFECYCLE.items():
        print(f"\n{'─' * 65}")
        print(f"  {phase['name'].upper()}")
        print(f"  Objective: {phase['objective']}")
        print(f"{'─' * 65}")

        if "checklist" in phase:
            for i, item in enumerate(phase["checklist"], 1):
                print(f"  [ ] {i:>2}. {item}")

        # Phase 3 has sub-checklists
        for sub_key in ["containment_checklist", "eradication_checklist", "recovery_checklist"]:
            if sub_key in phase:
                sub_name = sub_key.replace("_checklist", "").title()
                print(f"\n  >> {sub_name}:")
                for i, item in enumerate(phase[sub_key], 1):
                    print(f"  [ ] {i:>2}. {item}")

    print(f"\n{'=' * 65}")


if __name__ == "__main__":
    display_lifecycle()

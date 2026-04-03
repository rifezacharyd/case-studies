"""
Purdue Model Visualization

Generates an ASCII visualization of the Purdue Enterprise Reference
Architecture used for ICS/OT network segmentation.
"""


def render_purdue_model():
    """Display the Purdue Model as an ASCII diagram."""
    width = 66

    model = """
╔══════════════════════════════════════════════════════════════════╗
║            PURDUE ENTERPRISE REFERENCE ARCHITECTURE             ║
║              (ICS Network Segmentation Model)                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  LEVEL 5 — Enterprise Network                                   ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │  Internet connectivity, cloud services, remote access      │  ║
║  └────────────────────────┬───────────────────────────────────┘  ║
║                           │                                      ║
║  LEVEL 4 — Enterprise IT  │                                      ║
║  ┌────────────────────────┴───────────────────────────────────┐  ║
║  │  Email, ERP, business applications, corporate network      │  ║
║  └────────────────────────┬───────────────────────────────────┘  ║
║                           │                                      ║
║  ╔════════════════════════╪═══════════════════════════════════╗  ║
║  ║        IT/OT DEMILITARIZED ZONE (DMZ)                     ║  ║
║  ║  ┌──────────────────────────────────────────────────────┐ ║  ║
║  ║  │  Data historian mirror, jump servers, patch mgmt,    │ ║  ║
║  ║  │  antivirus relay, remote access gateway              │ ║  ║
║  ║  └──────────────────────────────────────────────────────┘ ║  ║
║  ╚════════════════════════╪═══════════════════════════════════╝  ║
║                           │                                      ║
║  LEVEL 3 — Site Operations                                       ║
║  ┌────────────────────────┴───────────────────────────────────┐  ║
║  │  Data historian, engineering workstations, OT domain       │  ║
║  │  controller, file servers, patch management                │  ║
║  └────────────────────────┬───────────────────────────────────┘  ║
║                           │                                      ║
║  LEVEL 2 — Area Supervisory Control                              ║
║  ┌────────────────────────┴───────────────────────────────────┐  ║
║  │  HMI (Human-Machine Interface), SCADA servers,            │  ║
║  │  alarm servers, operator consoles                          │  ║
║  └────────────────────────┬───────────────────────────────────┘  ║
║                           │                                      ║
║  LEVEL 1 — Basic Control                                         ║
║  ┌────────────────────────┴───────────────────────────────────┐  ║
║  │  PLCs, RTUs, DCS controllers, safety systems (SIS)        │  ║
║  └────────────────────────┬───────────────────────────────────┘  ║
║                           │                                      ║
║  LEVEL 0 — Physical Process                                      ║
║  ┌────────────────────────┴───────────────────────────────────┐  ║
║  │  Sensors, actuators, valves, motors, physical equipment    │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

KEY SECURITY PRINCIPLES:
  • Traffic should only flow between adjacent levels
  • The DMZ prevents direct IT-to-OT communication
  • Level 0-1 devices often lack authentication/encryption
  • Each level boundary is a firewall enforcement point
  • Lateral movement across levels indicates compromise
"""
    print(model)


if __name__ == "__main__":
    render_purdue_model()

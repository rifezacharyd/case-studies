"""
Critical Infrastructure Sectors Data Model

Models all 16 critical infrastructure sectors as defined by
Presidential Policy Directive 21 (PPD-21), including their
Sector Risk Management Agencies and key interdependencies.
"""

SECTORS = {
    "energy": {
        "name": "Energy",
        "srma": "Department of Energy (DOE)",
        "description": "Electricity, oil, and natural gas production, refining, storage, and distribution",
        "dependencies": ["communications", "information_technology", "transportation", "water"],
        "key_risks": ["Grid disruption", "Pipeline attacks", "SCADA exploitation"],
    },
    "water": {
        "name": "Water and Wastewater Systems",
        "srma": "Environmental Protection Agency (EPA)",
        "description": "Drinking water and wastewater treatment and distribution",
        "dependencies": ["energy", "chemicals", "transportation"],
        "key_risks": ["Treatment process manipulation", "Chemical dosing attacks"],
    },
    "transportation": {
        "name": "Transportation Systems",
        "srma": "Department of Transportation (DOT) / Department of Homeland Security (DHS)",
        "description": "Aviation, maritime, rail, highway, and public transit systems",
        "dependencies": ["energy", "communications", "information_technology"],
        "key_risks": ["Traffic management system attacks", "GPS spoofing", "Rail signaling"],
    },
    "communications": {
        "name": "Communications",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Telecommunications, broadcast, cable, satellite, and internet infrastructure",
        "dependencies": ["energy", "information_technology"],
        "key_risks": ["BGP hijacking", "Undersea cable sabotage", "5G infrastructure"],
    },
    "healthcare": {
        "name": "Healthcare and Public Health",
        "srma": "Department of Health and Human Services (HHS)",
        "description": "Hospitals, research facilities, pharmaceuticals, and public health networks",
        "dependencies": ["energy", "communications", "transportation", "water", "information_technology"],
        "key_risks": ["Ransomware disrupting patient care", "Medical device vulnerabilities"],
    },
    "financial_services": {
        "name": "Financial Services",
        "srma": "Department of the Treasury",
        "description": "Banking, securities, insurance, and payment systems",
        "dependencies": ["communications", "information_technology", "energy"],
        "key_risks": ["SWIFT network targeting", "Trading system manipulation"],
    },
    "food_agriculture": {
        "name": "Food and Agriculture",
        "srma": "Department of Agriculture (USDA) / Department of Health and Human Services (HHS)",
        "description": "Farms, food processing, storage, and distribution",
        "dependencies": ["water", "transportation", "energy", "chemicals"],
        "key_risks": ["Supply chain disruption", "Processing system manipulation"],
    },
    "government_facilities": {
        "name": "Government Facilities",
        "srma": "Department of Homeland Security (DHS) / General Services Administration (GSA)",
        "description": "Federal, state, and local government buildings and facilities",
        "dependencies": ["energy", "communications", "information_technology"],
        "key_risks": ["Physical access control bypass", "Building automation system attacks"],
    },
    "defense_industrial_base": {
        "name": "Defense Industrial Base",
        "srma": "Department of Defense (DoD)",
        "description": "Military weapons systems, R&D, and defense supply chain",
        "dependencies": ["energy", "communications", "information_technology", "transportation"],
        "key_risks": ["IP theft", "Supply chain compromise", "Classified network intrusion"],
    },
    "information_technology": {
        "name": "Information Technology",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Hardware, software, IT systems and services, and internet infrastructure",
        "dependencies": ["energy", "communications"],
        "key_risks": ["Supply chain attacks", "DNS infrastructure", "Cloud provider compromise"],
    },
    "nuclear": {
        "name": "Nuclear Reactors, Materials, and Waste",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Nuclear power plants, materials, and waste management",
        "dependencies": ["energy", "transportation", "water"],
        "key_risks": ["Safety system manipulation", "Material diversion"],
    },
    "chemicals": {
        "name": "Chemical",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Chemical manufacturing, storage, and distribution",
        "dependencies": ["energy", "transportation", "water"],
        "key_risks": ["Process safety manipulation", "TRITON-style SIS attacks"],
    },
    "commercial_facilities": {
        "name": "Commercial Facilities",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Entertainment, lodging, retail, and large public venues",
        "dependencies": ["energy", "communications", "water"],
        "key_risks": ["Physical security system compromise", "POS system attacks"],
    },
    "critical_manufacturing": {
        "name": "Critical Manufacturing",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Primary metals, machinery, electrical equipment, and transportation equipment manufacturing",
        "dependencies": ["energy", "transportation", "information_technology"],
        "key_risks": ["ICS manipulation", "Production sabotage", "IP theft"],
    },
    "dams": {
        "name": "Dams",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Dam projects, navigation locks, levees, and flood control systems",
        "dependencies": ["energy", "water", "communications"],
        "key_risks": ["Control system manipulation", "Structural monitoring interference"],
    },
    "emergency_services": {
        "name": "Emergency Services",
        "srma": "Department of Homeland Security (DHS)",
        "description": "Law enforcement, fire, EMS, and emergency management",
        "dependencies": ["communications", "information_technology", "transportation", "energy"],
        "key_risks": ["911 system disruption", "CAD system attacks", "Radio jamming"],
    },
}


def display_sectors():
    """Display all sectors with their SRMAs."""
    print("=" * 70)
    print("  16 CRITICAL INFRASTRUCTURE SECTORS (PPD-21)")
    print("=" * 70)
    for i, (key, sector) in enumerate(SECTORS.items(), 1):
        print(f"\n  {i:>2}. {sector['name']}")
        print(f"      SRMA: {sector['srma']}")
        print(f"      Risks: {', '.join(sector['key_risks'])}")


def show_dependencies(sector_key: str):
    """Show what a given sector depends on."""
    if sector_key not in SECTORS:
        print(f"Unknown sector: {sector_key}")
        return
    sector = SECTORS[sector_key]
    print(f"\n{sector['name']} depends on:")
    for dep in sector["dependencies"]:
        print(f"  -> {SECTORS[dep]['name']}")


def find_most_depended():
    """Find which sectors are depended on most by others."""
    counts = {}
    for sector in SECTORS.values():
        for dep in sector["dependencies"]:
            counts[dep] = counts.get(dep, 0) + 1

    print("\nMost critical dependencies (sectors depended on by others):")
    for key, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {SECTORS[key]['name']}: depended on by {count} sector(s)")


if __name__ == "__main__":
    display_sectors()
    print()
    find_most_depended()

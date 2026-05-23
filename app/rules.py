# Regional and methodology constraints inspired by deeptech MRV demands
COMPLIANCE_KEYWORDS = {
    "methodologies": ["VM0044", "VM0042", "Gold Standard", "GHG Protocol"],
    "required_streams": {
        "biochar": ["pyrolysis temperature", "feedstock weight", "kiln thermal status"],
        "soil": ["soil moisture", "bulk density", "pH", "organic carbon"],
        "agroforestry": ["canopy cover", "tree diameter", "species mix", "beehive activity"]
    },
    "critical_risks": {
        "leakage": "High risk of project activity shifting emissions outside boundary.",
        "permanence": "Reversal risks identified (e.g., wildfire zone, dynamic soil erosion).",
        "additionality": "Unclear baseline context; verification may be contested legally."
    }
}

class RegulatoryIntelligence:
    """
    Evaluates unstructured field context against verification frameworks
    to output deterministic configuration baselines.
    """
    @staticmethod
    def identify_required_sensors(text: str) -> list[str]:
        text_lower = text.lower()
        sensors = set()
        
        # Determine sensor infrastructure needs based on site operational description
        if any(w in text_lower for w in ["kiln", "pyrolysis", "biochar", "burn"]):
            sensors.update(["thermal_probe_high_temp", "feedstock_scale_weight"])
        if any(w in text_lower for w in ["soil", "agri", "farm", "crop", "roots"]):
            sensors.update(["soil_moisture_sensor", "soil_ph_probe", "co2_flux_sensor"])
        if any(w in text_lower for w in ["tree", "forest", "canopy", "bee", "beehive"]):
            sensors.update(["lidar_optical_node", "acoustic_beehive_monitor"])
            
        return list(sensors) if sensors else ["generic_environmental_tracker"]

    @staticmethod
    def assess_kill_logic_triggers(text: str) -> list[str]:
        text_lower = text.lower()
        triggers = []
        
        # Propose immediate drop filters if structural integrity cannot be proven
        if "gps" not in text_lower and "boundary" not in text_lower and "parcel" not in text_lower:
            triggers.append("MISSING_GEOSPATIAL_BOUNDARY: Cannot verify parcel provenance.")
        if "calibration" not in text_lower and "baseline" not in text_lower:
            triggers.append("UNVERIFIED_SENSOR_BASELINE: Risks sensor drift contamination.")
        if "leakage" in text_lower:
            triggers.append("UNMITIGATED_LEAKAGE_RISK: External baseline shifting detected.")
            
        return triggers
import re
from .rules import COMPLIANCE_KEYWORDS, RegulatoryIntelligence

class MissionReportParser:
    """
    Probabilistic text analytics engine that processes unstructured text 
    from MRV field missions and maps them to deterministic environmental constraints.
    """
    
    @staticmethod
    def analyze_document(text_content: str) -> dict:
        text_lower = text_content.lower()
        
        # 1. Detect Regulatory Methodologies
        detected_methodologies = []
        for method in COMPLIANCE_KEYWORDS["methodologies"]:
            if method.lower() in text_lower:
                detected_methodologies.append(method)
        
        # If none detected, default to standard GHG Protocol baseline
        if not detected_methodologies:
            detected_methodologies.append("GHG Protocol Baseline Standard")

        # 2. Extract Sensor Infrastructure Requirements
        recommended_sensors = RegulatoryIntelligence.identify_required_sensors(text_content)

        # 3. Assess Compliance Risk Flags & Proposed Edge KILL Logic
        proposed_kill_triggers = RegulatoryIntelligence.assess_kill_logic_triggers(text_content)

        # 4. Map Contextual Missing Fields
        missing_data_gaps = []
        if "ph" not in text_lower and "soil" in text_lower:
            missing_data_gaps.append("pH baseline dynamics")
        if "bulk density" not in text_lower and "soil" in text_lower:
            missing_data_gaps.append("Soil core bulk density measurements")
        if "moisture" not in text_lower and "soil" in text_lower:
            missing_data_gaps.append("Continuous moisture telemetry integration")
        if "temperature" not in text_lower and "kiln" in text_lower:
            missing_data_gaps.append("Pyrolysis peak thermal tracking parameters")

        # Systemic assessment classification
        risk_score = "LOW"
        if len(proposed_kill_triggers) >= 2:
            risk_score = "HIGH"
        elif len(proposed_kill_triggers) == 1:
            risk_score = "MEDIUM"

        return {
            "metadata_extraction": {
                "detected_frameworks": detected_methodologies,
                "contextual_risk_classification": risk_score
            },
            "infrastructure_mapping": {
                "required_edge_sensors": recommended_sensors,
                "missing_operational_parameters": missing_data_gaps
            },
            "proposed_edge_kill_logic": proposed_kill_triggers
        }
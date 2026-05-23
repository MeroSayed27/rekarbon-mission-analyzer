from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from .parser import MissionReportParser
from datetime import datetime

app = FastAPI(
    title="REKARBON Cloud-Layer Mission Analyzer Prototype",
    description="Probabilistic intelligence engine extracting deterministic sensor configurations from unstructured field reports.",
    version="1.0"
)

# =========================================
# DATA CONTRACTS
# =========================================

class MissionReportPayload(BaseModel):
    reporter_id: str = Field(..., example="FIELD-ENG-MOHAMMED")
    raw_text: str = Field(..., example=(
        "We are launching a new multi-site pilot program in Madagascar. "
        "The site contains agricultural cooperatives focusing on biochar production "
        "using local kilns. Soil parameters look stable, but we noticed local "
        "leakage risks near the forest boundary. No GPS coordinates verified yet."
    ))

# =========================================
# ENDPOINTS
# =========================================

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {
        "subsystem": "REKARBON Cloud Intelligence Layer",
        "status": "operational",
        "analysis_rules_loaded": True,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.post("/api/v1/analyze-mission", status_code=status.HTTP_200_OK)
async def analyze_field_mission(payload: MissionReportPayload):
    if not payload.raw_text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Payload text content cannot be blank."
        )

    # Process unstructured text using rule-based parsing engine
    analysis_result = MissionReportParser.analyze_document(payload.raw_text)
    
    return {
        "processed_by": payload.reporter_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "analysis": analysis_result
    }
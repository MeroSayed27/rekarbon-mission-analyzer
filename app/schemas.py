from pydantic import BaseModel, Field
from datetime import datetime

class SensorPayload(BaseModel):
    """
    Data contract for incoming environmental sensor telemetry.
    Pydantic automatically handles missing value validation and type casting.
    """
    site_id: str = Field(..., description="Unique identifier for the physical monitoring site", example="MADAGASCAR-SITE-A")
    sensor_id: str = Field(..., description="Unique hardware identifier for the IoT node", example="NODE-RPI5-042")
    temperature: float = Field(..., description="Ambient temperature reading in Celsius", example=24.5)
    co2: float = Field(..., description="Carbon dioxide concentration in parts per million (PPM)", example=415.0)

    class Config:
        json_schema_extra = {
            "example": {
                "site_id": "MADAGASCAR-SITE-A",
                "sensor_id": "NODE-RPI5-042",
                "temperature": 24.5,
                "co2": 415.0
            }
        }
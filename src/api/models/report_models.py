from pydantic import BaseModel, Field
from typing import Literal, List
from typing import Dict

class ReportSummary(BaseModel):

    report_id: str
    patient_name: str
    age: int
    gender: str
    condition: str
    severity: str


class ReportListResponse(BaseModel):

    page: int
    limit: int
    total_reports: int
    total_pages: int
    reports: list[ReportSummary]



class ReportUpdate(BaseModel):

    patient_name: str
    age: int
    gender: str
    condition: str
    severity: str


class CBCInput(BaseModel):

    Age: int = Field(..., ge=1, le=120)

    Gender: Literal["Male", "Female"]

    Hemoglobin: float = Field(..., ge=3, le=20)

    WBC: float = Field(..., ge=1000, le=100000)

    RBC: float = Field(..., ge=1.0, le=8.0)

    Platelets: float = Field(..., ge=10000, le=1000000)

    Hematocrit: float = Field(..., ge=10, le=70)

    MCV: float = Field(..., ge=50, le=130)

    MCH: float = Field(..., ge=15, le=45)

    MCHC: float = Field(..., ge=20, le=40)



class PredictionResponse(BaseModel):

    prediction: str
    confidence: float
    confidence_level: str
    severity: str
    findings: List[str]
    summary: str
    recommendation: str
    important_features: List[Dict]
from typing import Literal

from pydantic import BaseModel, Field


class ReportSummary(BaseModel):
    report_id: str = Field(
        ...,
        description="Unique report identifier",
        examples=["RPT-20260728-001"],
    )

    patient_name: str = Field(
        ...,
        description="Patient full name",
        examples=["John Doe"],
    )

    age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Patient age in years",
        examples=[35],
    )

    gender: str = Field(
        ...,
        description="Patient gender",
        examples=["Male"],
    )

    condition: str = Field(
        ...,
        description="Predicted medical condition",
        examples=["Healthy"],
    )

    severity: str = Field(
        ...,
        description="Severity level of the predicted condition",
        examples=["Normal"],
    )


class ReportListResponse(BaseModel):
    page: int = Field(..., description="Current page number")
    limit: int = Field(..., description="Reports per page")
    total_reports: int = Field(..., description="Total available reports")
    total_pages: int = Field(..., description="Total available pages")
    reports: list[ReportSummary]

    model_config = {
        "json_schema_extra": {
            "example": {
                "page": 1,
                "limit": 10,
                "total_reports": 52,
                "total_pages": 6,
                "reports": [
                    {
                        "report_id": "RPT-20260728-001",
                        "patient_name": "John Doe",
                        "age": 35,
                        "gender": "Male",
                        "condition": "Healthy",
                        "severity": "Normal",
                    }
                ],
            }
        }
    }


class ReportUpdate(BaseModel):
    patient_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Updated patient name",
        examples=["John Doe"],
    )

    age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Updated patient age",
        examples=[35],
    )

    gender: str = Field(
        ...,
        description="Updated patient gender",
        examples=["Male"],
    )

    condition: str = Field(
        ...,
        description="Updated medical condition",
        examples=["Healthy"],
    )

    severity: str = Field(
        ...,
        description="Updated severity level",
        examples=["Normal"],
    )


class CBCInput(BaseModel):
    Age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Patient age",
        examples=[35],
    )

    Gender: Literal["Male", "Female"] = Field(
        ...,
        description="Patient gender",
        examples=["Male"],
    )

    Hemoglobin: float = Field(
        ...,
        ge=3,
        le=20,
        description="Hemoglobin (g/dL)",
        examples=[14.2],
    )

    WBC: float = Field(
        ...,
        ge=1000,
        le=100000,
        description="White Blood Cell count",
        examples=[7200],
    )

    RBC: float = Field(
        ...,
        ge=1.0,
        le=8.0,
        description="Red Blood Cell count",
        examples=[5.1],
    )

    Platelets: float = Field(
        ...,
        ge=10000,
        le=1000000,
        description="Platelet count",
        examples=[250000],
    )

    Hematocrit: float = Field(
        ...,
        ge=10,
        le=70,
        description="Hematocrit (%)",
        examples=[42.0],
    )

    MCV: float = Field(
        ...,
        ge=50,
        le=130,
        description="Mean Corpuscular Volume (fL)",
        examples=[90.5],
    )

    MCH: float = Field(
        ...,
        ge=15,
        le=45,
        description="Mean Corpuscular Hemoglobin (pg)",
        examples=[30.2],
    )

    MCHC: float = Field(
        ...,
        ge=20,
        le=40,
        description="Mean Corpuscular Hemoglobin Concentration (g/dL)",
        examples=[33.5],
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "Age": 35,
                "Gender": "Male",
                "Hemoglobin": 14.2,
                "WBC": 7200,
                "RBC": 5.1,
                "Platelets": 250000,
                "Hematocrit": 42.0,
                "MCV": 90.5,
                "MCH": 30.2,
                "MCHC": 33.5,
            }
        }
    }


class PredictionResponse(BaseModel):
    prediction: str = Field(
        ...,
        description="Predicted medical condition",
        examples=["Healthy"],
    )

    confidence: float = Field(
        ...,
        description="Prediction confidence percentage",
        examples=[98.73],
    )

    confidence_level: str = Field(
        ...,
        description="Confidence category",
        examples=["High"],
    )

    severity: str = Field(
        ...,
        description="Predicted severity level",
        examples=["Normal"],
    )

    findings: list[str] = Field(
        ...,
        description="Important findings from CBC analysis",
    )

    summary: str = Field(
        ...,
        description="AI-generated medical summary",
    )

    recommendation: str = Field(
        ...,
        description="Recommended next step",
    )

    important_features: list[dict] = Field(
        ...,
        description="Most influential CBC parameters used during prediction",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "prediction": "Healthy",
                "confidence": 98.73,
                "confidence_level": "High",
                "severity": "Normal",
                "findings": [
                    "All CBC parameters are within the normal reference range."
                ],
                "summary": "CBC analysis indicates a healthy blood profile.",
                "recommendation": "Continue routine health checkups.",
                "important_features": [
                    {
                        "feature": "Hemoglobin",
                        "value": 14.2,
                    },
                    {
                        "feature": "WBC",
                        "value": 7200,
                    },
                ],
            }
        }
    }
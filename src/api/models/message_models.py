
from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    message: str = Field(
        ...,
        description="Operation result message",
        examples=["Report deleted successfully"],
    )

    report_id: str = Field(
        ...,
        description="Unique report identifier",
        examples=["R00049"],
    )


class HomeResponse(BaseModel):
    success: bool = Field(
        ...,
        description="API availability status",
        examples=[True],
    )

    message: str = Field(
        ...,
        description="API status message",
        examples=["AI-Powered Medical Report Generator API is running"],
    )

    version: str = Field(
        ...,
        description="Application version",
        examples=["1.0.0"],
    )

    api_version: str = Field(
        ...,
        description="API version",
        examples=["v1"],
    )

    documentation: str = Field(
        ...,
        description="Swagger documentation endpoint",
        examples=["/docs"],
    )

    redoc: str = Field(
        ...,
        description="ReDoc documentation endpoint",
        examples=["/redoc"],
    )

    base_url: str = Field(
        ...,
        description="API base URL",
        examples=["/api/v1"],
    )


class HealthResponse(BaseModel):
    status: str = Field(
        ...,
        description="Health status",
        examples=["healthy"],
    )

    service: str = Field(
        ...,
        description="Service name",
        examples=["AI-Powered Medical Report Generator API"],
    )

    api_version: str = Field(
        ...,
        description="Current API version",
        examples=["v1"],
    )

    version: str = Field(
        ...,
        description="Application version",
        examples=["1.0.0"],
    )


class StatisticsResponse(BaseModel):
    total_reports: int = Field(
        ...,
        description="Total number of reports",
        examples=[49],
    )

    average_age: float = Field(
        ...,
        description="Average patient age",
        examples=[36.8],
    )

    male: int = Field(
        ...,
        description="Number of male patients",
        examples=[28],
    )

    female: int = Field(
        ...,
        description="Number of female patients",
        examples=[21],
    )

    conditions: dict[str, int] = Field(
        ...,
        description="Condition-wise report count",
        examples=[
            {
                "Healthy": 18,
                "Iron Deficiency": 10,
                "Leukocytosis": 7,
                "Leukopenia": 6,
                "Viral Infection": 5,
                "Thrombocytopenia": 3,
            }
        ],
    )
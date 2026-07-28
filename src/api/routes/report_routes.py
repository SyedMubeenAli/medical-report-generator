from math import ceil

from fastapi import APIRouter, Path, Query

from src.ai.predictor import predict_condition
from src.api.models.message_models import (
    MessageResponse,
    StatisticsResponse,
)
from src.api.models.report_models import (
    CBCInput,
    PredictionResponse,
    ReportListResponse,
    ReportUpdate,
)
from src.api.services.report_service import (
    delete_report,
    get_all_reports,
    get_report,
    get_statistics,
    update_report,
)
from src.core.exceptions import (
    ReportNotFoundException,
)

router = APIRouter(
    prefix="/reports",
    tags=["Medical Reports"],
    responses={
        404: {"description": "Report not found"},
        422: {"description": "Validation error"},
        500: {"description": "Internal server error"},
    },
)


@router.get(
    "/",
    response_model=ReportListResponse,
    summary="Get All Medical Reports",
    description="""
Retrieve a paginated list of generated medical reports.

### Features
- Pagination
- Filter by patient name
- Filter by medical condition
- Sort by supported fields
- Ascending or descending order
""",
    response_description="Paginated list of medical reports",
    responses={
        200: {
            "description": "Medical reports retrieved successfully"
        }
    },
)
def read_all_reports(
    page: int = Query(
        1,
        ge=1,
        description="Page number",
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Number of reports per page",
    ),
    patient: str | None = Query(
        None,
        description="Filter by patient name",
    ),
    condition: str | None = Query(
        None,
        description="Filter by predicted medical condition",
    ),
    sort_by: str | None = Query(
        None,
        description="Field used for sorting",
    ),
    order: str = Query(
        "asc",
        description="Sorting order (asc or desc)",
    ),
):
    reports = get_all_reports(
        patient=patient,
        condition=condition,
        sort_by=sort_by,
        order=order,
    )

    total_reports = len(reports)
    total_pages = ceil(total_reports / limit) if total_reports else 1

    start = (page - 1) * limit
    end = start + limit

    paginated_reports = reports[start:end]

    return {
        "page": page,
        "limit": limit,
        "total_reports": total_reports,
        "total_pages": total_pages,
        "reports": paginated_reports,
    }


@router.get(
    "/stats",
    response_model=StatisticsResponse,
    summary="Get Report Statistics",
    description="""
Retrieve aggregated statistics for all stored medical reports.

Includes report count and condition-wise distribution.
""",
    response_description="Statistics generated successfully",
    responses={
        200: {
            "description": "Statistics retrieved successfully"
        }
    },
)
def read_statistics():
    return get_statistics()


@router.get(
    "/{report_id}",
    summary="Get Medical Report",
    description="""
Retrieve a single medical report using its unique Report ID.
""",
    response_description="Medical report retrieved successfully",
    responses={
        200: {
            "description": "Report found"
        },
        404: {
            "description": "Report not found"
        },
    },
)
def read_report(
    report_id: str = Path(
        ...,
        description="Unique Report ID",
    ),
):
    report = get_report(report_id)

    if report is None:
        raise ReportNotFoundException()
    
    return report


@router.put(
    "/{report_id}",
    summary="Update Existing Report",
    description="Update an existing medical report.",
)
def update_existing_report(
    report_id: str = Path(
        ...,
        description="Unique Report ID",
    ),
    report_data: ReportUpdate = ...,
):
    report = update_report(
        report_id,
        report_data.model_dump(),
    )

    if report is None:
        raise ReportNotFoundException()

    return report


@router.delete(
    "/{report_id}",
    response_model=MessageResponse,
    summary="Delete Report",
    description="Delete a medical report using its Report ID.",
)
def remove_report(
    report_id: str = Path(
        ...,
        description="Unique Report ID",
    ),
):
    success = delete_report(report_id)

    if not success:
        raise ReportNotFoundException()

    return {
        "message": "Report deleted successfully",
        "report_id": report_id,
    }


@router.post(
    "/analyze",
    response_model=PredictionResponse,
    summary="Analyze CBC Report",
    description="""
Predict the most likely medical condition from CBC parameters using the trained Machine Learning model.
""",
    response_description="Prediction generated successfully",
    responses={
        200: {
            "description": "Prediction completed successfully"
        }
    },
)
def analyze_report(data: CBCInput):
    prediction = predict_condition(data.model_dump())
    return prediction
from math import ceil

from fastapi import APIRouter, HTTPException, Query

from src.api.services.report_service import (
    get_report,
    get_all_reports,
    get_statistics,
    update_report,
    delete_report
)

from src.api.models.report_models import (
    ReportListResponse,
    ReportSummary,
    ReportUpdate,
    CBCInput,
    PredictionResponse
)

from src.api.models.message_models import MessageResponse

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

from src.ai.predictor import predict_condition


@router.get(
    "/",
    response_model=ReportListResponse
)

def read_all_reports( 
    

    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    patient: str | None = None,
    condition: str | None = None,
    sort_by: str | None = None,
    order: str = "asc"
    

):


    reports = get_all_reports(
        patient=patient,
        condition=condition,
        sort_by=sort_by,
        order=order
    )

    total_reports = len(reports)
    total_pages = ceil(total_reports / limit)

    start = (page - 1) * limit
    end = start + limit

    paginated_reports = reports[start:end]

    return {

        "page": page,
        "limit": limit,
        "total_reports": total_reports,
        "total_pages": total_pages,
        "reports": paginated_reports

    }

@router.get("/stats")

def read_statistics():

    return get_statistics()


@router.get("/{report_id}")
def read_report(report_id: str):

    report = get_report(report_id)

    if report is None:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return report

@router.put("/{report_id}")

def update_existing_report(
    report_id: str,
    report_data: ReportUpdate
):

    report = update_report(
        report_id,
        report_data.model_dump()
    )

    if report is None:

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return report


@router.delete(
    "/{report_id}",
    response_model=MessageResponse
)
def remove_report(report_id: str):

    success = delete_report(report_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "message": "Report deleted successfully",
        "report_id": report_id
    }


@router.post(
    "/analyze",
    response_model=PredictionResponse
)
def analyze_report(data: CBCInput):

    prediction = predict_condition(
        data.model_dump()
    )

    return prediction
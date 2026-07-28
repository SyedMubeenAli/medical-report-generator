from fastapi import HTTPException


class ReportNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Report not found"
        )


class InvalidReportException(HTTPException):
    def __init__(self, message: str = "Invalid report data"):
        super().__init__(
            status_code=400,
            detail=message
        )


class PredictionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=500,
            detail="Failed to generate AI prediction"
        )


class ExportException(HTTPException):
    def __init__(self, export_type: str):
        super().__init__(
            status_code=500,
            detail=f"Failed to export report as {export_type}"
        )
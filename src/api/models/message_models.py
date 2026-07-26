from pydantic import BaseModel


class MessageResponse(BaseModel):

    message: str
    report_id: str
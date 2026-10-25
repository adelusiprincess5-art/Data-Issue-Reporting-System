from pydantic import BaseModel


class DataIssueCreate(BaseModel):
    title: str
    description: str
    issue_type: str
    severity: str
    reported_by: str


class DataIssueUpdate(BaseModel):
    status: str


class DataIssueResponse(BaseModel):
    id: int
    title: str
    description: str
    issue_type: str
    severity: str
    reported_by: str
    status: str

    class Config:
        from_attributes = True
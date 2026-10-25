from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import DataIssue
from schemas import (
    DataIssueCreate,
    DataIssueUpdate,
    DataIssueResponse
)


router = APIRouter(
    prefix="/issues",
    tags=["Data Issues"]
)


@router.post("/", response_model=DataIssueResponse)
def create_issue(
    issue: DataIssueCreate,
    db: Session = Depends(get_db)
):
    new_issue = DataIssue(
        title=issue.title,
        description=issue.description,
        issue_type=issue.issue_type,
        severity=issue.severity,
        reported_by=issue.reported_by
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return new_issue


@router.get("/", response_model=list[DataIssueResponse])
def get_issues(
    db: Session = Depends(get_db)
):
    return db.query(DataIssue).all()


@router.get("/{issue_id}", response_model=DataIssueResponse)
def get_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = db.query(DataIssue).filter(
        DataIssue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Data issue not found"
        )

    return issue


@router.put("/{issue_id}", response_model=DataIssueResponse)
def update_issue(
    issue_id: int,
    issue_data: DataIssueUpdate,
    db: Session = Depends(get_db)
):
    issue = db.query(DataIssue).filter(
        DataIssue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Data issue not found"
        )

    allowed_statuses = {
        "Open",
        "Investigating",
        "Resolved",
        "Closed"
    }

    if issue_data.status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    issue.status = issue_data.status

    db.commit()
    db.refresh(issue)

    return issue


@router.delete("/{issue_id}")
def delete_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = db.query(DataIssue).filter(
        DataIssue.id == issue_id
    ).first()

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Data issue not found"
        )

    db.delete(issue)
    db.commit()

    return {
        "message": "Data issue deleted successfully"
    }
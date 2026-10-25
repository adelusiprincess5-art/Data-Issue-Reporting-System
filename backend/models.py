from sqlalchemy import Column, Integer, String, Text

from database import Base


class DataIssue(Base):
    __tablename__ = "data_issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    issue_type = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    reported_by = Column(String, nullable=False)
    status = Column(String, default="Open", nullable=False)
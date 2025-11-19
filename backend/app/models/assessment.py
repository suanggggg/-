from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.sqlite import JSON
from app.db.base import Base
import uuid
from datetime import datetime, timezone


class Assessment(Base):
    __tablename__ = "assessments"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    type = Column(String, nullable=True)
    start_time = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    end_time = Column(DateTime(timezone=True), nullable=True)
    media_ref = Column(String, nullable=True)
    system_score = Column(JSON, nullable=True)

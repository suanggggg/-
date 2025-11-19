from sqlalchemy import Column, String, Integer, Text, DateTime
from app.db.base import Base
import uuid
from datetime import datetime


class Question(Base):
    __tablename__ = "questions"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    body = Column(Text, nullable=True)
    choices = Column(Text, nullable=True)  # JSON string or newline-separated
    answer = Column(String, nullable=True)
    difficulty = Column(Integer, default=1)
    tags = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

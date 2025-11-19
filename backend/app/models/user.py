from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.db.base import Base
import enum
import uuid
from datetime import datetime


class UserRole(enum.Enum):
    admin = "admin"
    operator = "operator"
    expert = "expert"
    learner = "learner"


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    contact_account = Column(String, nullable=True)
    birth_md = Column(String, nullable=True)  # 月日
    role = Column(Enum(UserRole), default=UserRole.learner)
    points_balance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

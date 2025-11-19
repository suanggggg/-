from sqlalchemy.orm import Session
from app.models.assessment import Assessment
from typing import List, Optional
from datetime import datetime


def create_assessment(db: Session, user_id: str, type: str = None, media_ref: str = None, system_score: dict = None) -> Assessment:
    a = Assessment(user_id=user_id, type=type, media_ref=media_ref, system_score=system_score)
    db.add(a)
    db.commit()
    db.refresh(a)
    return a


def get_assessment(db: Session, assessment_id: str) -> Optional[Assessment]:
    return db.query(Assessment).filter(Assessment.id == assessment_id).first()


def get_assessments_for_user(db: Session, user_id: str, skip: int = 0, limit: int = 100) -> List[Assessment]:
    return db.query(Assessment).filter(Assessment.user_id == user_id).offset(skip).limit(limit).all()


def update_assessment_system_score(db: Session, assessment_id: str, system_score: dict, end_time=None) -> Optional[Assessment]:
    a = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    if not a:
        return None
    a.system_score = system_score
    if end_time is not None:
        a.end_time = end_time
    db.add(a)
    db.commit()
    db.refresh(a)
    return a

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.api import deps
from app.schemas import assessment as schema
from app.crud import assessment as crud_assessment
from datetime import datetime, timezone

router = APIRouter()


@router.post("/", response_model=schema.AssessmentOut, status_code=status.HTTP_201_CREATED)
def create_assessment(a_in: schema.AssessmentCreate, db: Session = Depends(deps.get_db)):
    # 验证用户存在与否可在此处添加
    a = crud_assessment.create_assessment(db, user_id=a_in.user_id, type=a_in.type, media_ref=a_in.media_ref)
    return a


@router.get("/{assessment_id}", response_model=schema.AssessmentOut)
def read_assessment(assessment_id: str, db: Session = Depends(deps.get_db)):
    a = crud_assessment.get_assessment(db, assessment_id)
    if not a:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return a


@router.get("/user/{user_id}", response_model=List[schema.AssessmentOut])
def list_assessments_for_user(user_id: str, skip: int = 0, limit: int = 50, db: Session = Depends(deps.get_db)):
    return crud_assessment.get_assessments_for_user(db, user_id=user_id, skip=skip, limit=limit)


@router.post("/{assessment_id}/score", response_model=schema.AssessmentOut)
def submit_assessment_score(assessment_id: str, score_in: schema.AssessmentScore, db: Session = Depends(deps.get_db)):
    # 简单授权/验证可以在此处添加（例如只有面试官可打分）
    a = crud_assessment.update_assessment_system_score(db, assessment_id=assessment_id, system_score=score_in.system_score, end_time=datetime.now(timezone.utc))
    if not a:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return a


@router.get("/{assessment_id}/results", response_model=schema.AssessmentOut)
def get_assessment_results(assessment_id: str, db: Session = Depends(deps.get_db)):
    a = crud_assessment.get_assessment(db, assessment_id)
    if not a:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return a

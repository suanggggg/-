from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas import question as schema
from app.crud import question as crud_question

router = APIRouter()


@router.post("/", response_model=schema.QuestionOut, status_code=status.HTTP_201_CREATED)
def create_question(q_in: schema.QuestionCreate, db: Session = Depends(deps.get_db)):
    q = crud_question.create_question(db, title=q_in.title, body=q_in.body, choices=q_in.choices, answer=q_in.answer, difficulty=q_in.difficulty, tags=q_in.tags)
    return q


@router.get("/", response_model=List[schema.QuestionOut])
def list_questions(skip: int = 0, limit: int = 50, db: Session = Depends(deps.get_db)):
    return crud_question.get_questions(db, skip=skip, limit=limit)


@router.get("/{question_id}", response_model=schema.QuestionOut)
def read_question(question_id: str, db: Session = Depends(deps.get_db)):
    q = crud_question.get_question(db, question_id)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q


@router.put("/{question_id}", response_model=schema.QuestionOut)
def update_question(question_id: str, q_in: schema.QuestionUpdate, db: Session = Depends(deps.get_db)):
    # use Pydantic v2 model_dump for compatibility
    q = crud_question.update_question(db, question_id, **q_in.model_dump())
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: str, db: Session = Depends(deps.get_db)):
    ok = crud_question.delete_question(db, question_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Question not found")
    return None


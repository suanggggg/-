from sqlalchemy.orm import Session
from app.models.question import Question
from typing import List, Optional


def create_question(db: Session, *, title: str, body: str = None, choices: str = None, answer: str = None, difficulty: int = 1, tags: str = None) -> Question:
    q = Question(title=title, body=body, choices=choices, answer=answer, difficulty=difficulty, tags=tags)
    db.add(q)
    db.commit()
    db.refresh(q)
    return q


def get_question(db: Session, question_id: str) -> Optional[Question]:
    return db.query(Question).filter(Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100) -> List[Question]:
    return db.query(Question).offset(skip).limit(limit).all()


def update_question(db: Session, question_id: str, **updates) -> Optional[Question]:
    q = get_question(db, question_id)
    if not q:
        return None
    for k, v in updates.items():
        if hasattr(q, k) and v is not None:
            setattr(q, k, v)
    db.add(q)
    db.commit()
    db.refresh(q)
    return q


def delete_question(db: Session, question_id: str) -> bool:
    q = get_question(db, question_id)
    if not q:
        return False
    db.delete(q)
    db.commit()
    return True

# CRUD: User 相关操作

from sqlalchemy.orm import Session
from app.models.user import User
from typing import Optional


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user(db: Session, user_id: str) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, username: str, hashed_password: str, phone: str = None, role: str = "learner") -> User:
    user = User(username=username, hashed_password=hashed_password, phone=phone, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional


class QuestionBase(BaseModel):
    title: str
    body: Optional[str] = None
    choices: Optional[str] = None
    answer: Optional[str] = None
    difficulty: Optional[int] = 1
    tags: Optional[str] = None


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionOut(QuestionBase):
    id: str
    model_config = ConfigDict(from_attributes=True)

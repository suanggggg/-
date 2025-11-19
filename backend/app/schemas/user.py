from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional


class UserBase(BaseModel):
    username: str
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: str
    points_balance: int

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    sub: Optional[str] = None

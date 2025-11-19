from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime, timezone


class AssessmentBase(BaseModel):
    user_id: str
    type: Optional[str] = None
    media_ref: Optional[str] = None


class AssessmentCreate(AssessmentBase):
    pass


class AssessmentOut(AssessmentBase):
    id: str
    start_time: Optional[datetime]
    end_time: Optional[datetime]
    system_score: Optional[Dict[str, Any]]

    model_config = ConfigDict(from_attributes=True)


class AssessmentScore(BaseModel):
    system_score: Dict[str, Any]

    model_config = ConfigDict(from_attributes=True)

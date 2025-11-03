from pydantic import BaseModel
from datetime import datetime

class TalkBase(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime

class TalkCreate(TalkBase):
    speaker_id: int

class Talk(TalkBase):
    id: int
    speaker_id: int

    class Config:
        orm_mode = True
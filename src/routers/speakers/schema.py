from pydantic import BaseModel
from typing import List
from ..talks.schema import Talk

class SpeakerBase(BaseModel):
    name: str
    bio: str
    company: str

class SpeakerCreate(SpeakerBase):
    pass

class Speaker(SpeakerBase):
    id: int
    talks: List[Talk] = []

    class Config:
        orm_mode = True

class SpeakerWithTalks(Speaker):
    talks: List[Talk]
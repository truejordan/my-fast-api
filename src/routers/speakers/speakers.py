from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from . import schema
from ...database.database import get_db
from . import service

router = APIRouter(prefix="/speakers", tags=["speakers"])

@router.post("/", response_model=schema.Speaker)
def create_speaker(speaker: schema.SpeakerCreate, db: Session = Depends(get_db)):
    return service.create_speaker(speaker, db)

@router.get("/", response_model=List[schema.Speaker])
def read_speakers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.read_speakers(skip, limit, db)

@router.get("/{speaker_id}", response_model=schema.SpeakerWithTalks)
def read_speaker(speaker_id: int, db: Session = Depends(get_db)):
    return service.read_speaker(speaker_id, db)
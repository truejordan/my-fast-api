from fastapi import HTTPException
from sqlalchemy.orm import Session
from .model import Speaker
from . import schema

def create_speaker(speaker: schema.SpeakerCreate, db: Session):
    db_speaker = Speaker(**speaker.dict())
    db.add(db_speaker)
    db.commit()
    db.refresh(db_speaker)
    return db_speaker

def read_speakers(skip: int = 0, limit: int = 100, db: Session = None):
    speakers = db.query(Speaker).offset(skip).limit(limit).all()
    return speakers

def read_speaker(speaker_id: int, db: Session):
    db_speaker = db.query(Speaker).filter(Speaker.id == speaker_id).first()
    if db_speaker is None:
        raise HTTPException(status_code=404, detail="Speaker not found")
    return db_speaker
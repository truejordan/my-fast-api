from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .model import Talk
from . import schema
from ...database.database import get_db

def create_talk(talk: schema.TalkCreate, db: Session):
    db_talk = Talk(**talk.dict())
    db.add(db_talk)
    db.commit()
    db.refresh(db_talk)
    return db_talk

def read_talks(skip: int = 0, limit: int = 100, db: Session = None):
    talks = db.query(Talk).offset(skip).limit(limit).all()
    return talks

def read_talk(talk_id: int, db: Session):
    db_talk = db.query(Talk).filter(Talk.id == talk_id).first()
    if db_talk is None:
        raise HTTPException(status_code=404, detail="Talk not found")
    return db_talk
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from . import schema
from ...database.database import get_db
from . import service

router = APIRouter(prefix="/talks", tags=["talks"])

@router.post("/", response_model=schema.Talk)
def create_talk(talk: schema.TalkCreate, db: Session = Depends(get_db)):
    return service.create_talk(talk, db)

@router.get("/", response_model=List[schema.Talk])
def read_talks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.read_talks(skip, limit, db)

@router.get("/{talk_id}", response_model=schema.Talk)
def read_talk(talk_id: int, db: Session = Depends(get_db)):
    return service.read_talk(talk_id, db)
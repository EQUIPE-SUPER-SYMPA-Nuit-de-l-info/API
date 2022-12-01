from fastapi import APIRouter, Depends
from typing import List
from app.core.models.experience import Experience
from sqlalchemy.orm import Session
from app.core.postgres import crud
from app.core.postgres.main import get_db
router = APIRouter()

experiences = []

@router.post('/experience', tags=['experience'])
def creer_experience(experience: Experience, db: Session = Depends(get_db)):
    crud.creer_experience(db, experience.titre, experience.contenu)
    return "ok"

@router.get('/experiences', tags=['experience'])
def get_experiences(db: Session = Depends(get_db)):
    return crud.get_experiences(db)

from fastapi import APIRouter
from typing import List
from app.core.models.experience import Experience
router = APIRouter()

experiences = []

@router.post('/experience', tags=['experience'])
async def creer_experience(experience: Experience):
    experiences.append(experience)
    return "ok"

@router.get('/experiences', tags=['experience'], response_model=List[Experience])
async def get_experiences():
    return experiences

from sqlalchemy.orm import Session, joinedload
from .models.experience import Experience
import random

def creer_experience(db: Session, titre: str, contenu: str):
    db_experience = Experience(titre=titre, contenu=contenu)
    db.add(db_experience)
    db.commit()
    db.refresh(db_experience)
    return db_experience

def get_experiences(db: Session):
    experiences = db.query(Experience).all()
    return random.sample(experiences, 5)

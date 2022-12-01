from .models import Base
from .database import SessionLocal, engine

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:

        SessionLocal.remove()
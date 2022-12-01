from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from ..config import Parametre as param

# connection base de donne postgres hpa

POSTGRES_URL = f"postgresql://{param.postgres_username}:{param.postgres_username}@{param.postgres_url}/nuitinfo"

engine = create_engine(
    POSTGRES_URL
)
factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = scoped_session(factory)
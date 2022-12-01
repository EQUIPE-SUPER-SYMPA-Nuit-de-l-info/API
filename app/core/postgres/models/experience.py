from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from . import Base

class Experience(Base):
    __tablename__ = "experiences"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String)
    contenu = Column(String)


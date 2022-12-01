from pydantic import BaseModel, Field


class Experience(BaseModel):
    titre: str = Field(description="titre de l'éxperience", example="Ma première fois !")
    contenu: str = Field(description="Contenu explicatif de l'experience")
from pydantic import BaseModel, Field
from datetime import datetime


class ReadSpyCatSchema(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(min_length=1)
    years_of_experience: int = Field(ge=0)
    breed: str
    salary: int = Field(ge=0)
    created_at: datetime
    updated_at: datetime


class CreateSpyCatSchema(BaseModel):
    name: str = Field(min_length=1)
    years_of_experience: int = Field(ge=0)
    breed: str
    salary: int = Field(ge=0)


class UpdateSpyCatSchema(BaseModel):
    salary: int = Field(ge=0)

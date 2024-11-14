from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ReadTargetSchema(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(max_length=100)
    country: str = Field(max_length=100)
    complete: bool
    notes: str
    created_at: datetime
    updated_at: datetime


class CreateTargetSchema(BaseModel):
    name: str = Field(max_length=100)
    country: str = Field(max_length=100)
    notes: str


class CreateTargetForMissionSchema(CreateTargetSchema):
    mission_id: int


class UpdateTargetCompletionStatusSchema(BaseModel):
    complete: bool


class UpdateTargetSchema(BaseModel):
    notes: str

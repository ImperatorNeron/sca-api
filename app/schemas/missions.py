from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.schemas.targets import CreateTargetSchema, ReadTargetSchema


class ReadMissionSchema(BaseModel):
    id: int = Field(ge=0)
    spy_cat_id: Optional[int] = Field(None, ge=0)
    complete: bool = False
    created_at: datetime
    updated_at: datetime


class ReadMissionWithTargetsSchema(ReadMissionSchema):
    targets: list[ReadTargetSchema]


class CreateMissionSchema(BaseModel):
    spy_cat_id: Optional[int] = None
    complete: bool = False


class CreateMissionWithTargetsSchema(BaseModel):
    spy_cat_id: Optional[int] = None
    complete: bool = False
    targets: list[CreateTargetSchema]


class UpdateMissionSchema(BaseModel):
    spy_cat_id: Optional[int] = None
    complete: Optional[bool] = None
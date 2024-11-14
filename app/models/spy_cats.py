from app.models.base import BaseModel
from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, validates

from app.models.mixins import IdIntPkMixin, UpdateCreateDateTimeMixin
from app.schemas.spy_cats import ReadSpyCatSchema


class SpyCats(
    IdIntPkMixin,
    UpdateCreateDateTimeMixin,
    BaseModel,
):
    name: Mapped[str] = mapped_column(String(100), index=True)
    years_of_experience: Mapped[int] = mapped_column(Integer)
    breed: Mapped[str] = mapped_column(String(100))
    salary: Mapped[int] = mapped_column(Integer)

    @validates("breed")
    def validate_breed(self, key, breed):
        # TODO: parse from api
        allowed_breeds = ["Siamese", "Persian", "Maine Coon"]
        if breed not in allowed_breeds:
            # TODO: add custom validators
            raise ValueError("Invalid breed!")
        return breed

    def to_read_model(self):
        return ReadSpyCatSchema(
            id=self.id,
            name=self.name,
            years_of_experience=self.years_of_experience,
            breed=self.breed,
            salary=self.salary,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

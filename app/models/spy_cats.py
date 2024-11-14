from typing import TYPE_CHECKING
from app.models.base import BaseModel
from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.mixins import IdIntPkMixin, UpdateCreateDateTimeMixin
from app.schemas.spy_cats import ReadSpyCatSchema

if TYPE_CHECKING:
    from app.models.missions import Mission


class SpyCat(
    IdIntPkMixin,
    UpdateCreateDateTimeMixin,
    BaseModel,
):
    name: Mapped[str] = mapped_column(String(100), index=True)
    years_of_experience: Mapped[int] = mapped_column(Integer)
    breed: Mapped[str] = mapped_column(String(100))
    salary: Mapped[int] = mapped_column(Integer)

    mission: Mapped["Mission"] = relationship("Mission", back_populates="spy_cat")

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

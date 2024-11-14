from typing import TYPE_CHECKING
from sqlalchemy import Boolean, ForeignKey, String, Text
from app.models.base import BaseModel
from app.models.mixins import IdIntPkMixin, UpdateCreateDateTimeMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas.targets import ReadTargetSchema

if TYPE_CHECKING:
    from app.models.missions import Mission


class Target(
    IdIntPkMixin,
    UpdateCreateDateTimeMixin,
    BaseModel,
):
    name: Mapped[str] = mapped_column(String(100), index=True)
    country: Mapped[str] = mapped_column(String(100))
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    complete: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
    )

    mission_id: Mapped[int] = mapped_column(ForeignKey("missions.id"))
    mission: Mapped["Mission"] = relationship(
        "Mission",
        back_populates="targets",
    )

    def to_read_model(self):
        return ReadTargetSchema(
            id=self.id,
            name=self.name,
            country=self.country,
            notes=self.notes,
            complete=self.complete,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

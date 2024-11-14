from typing import TYPE_CHECKING
from sqlalchemy import Boolean, ForeignKey
from app.models.base import BaseModel
from app.models.mixins import IdIntPkMixin, UpdateCreateDateTimeMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas.missions import ReadMissionSchema


if TYPE_CHECKING:
    from app.models.spy_cats import SpyCat
    from app.models.targets import Target


class Mission(
    IdIntPkMixin,
    UpdateCreateDateTimeMixin,
    BaseModel,
):
    spy_cat_id: Mapped[int] = mapped_column(
        ForeignKey("spycats.id"),
        nullable=True,
    )
    complete: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
    )

    spy_cat: Mapped["SpyCat"] = relationship("SpyCat", back_populates="mission")
    targets: Mapped["Target"] = relationship(
        "Target",
        back_populates="mission",
        cascade="all, delete-orphan",
    )

    def to_read_model(self):
        return ReadMissionSchema(
            id=self.id,
            spy_cat_id=self.spy_cat_id,
            complete=self.complete,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

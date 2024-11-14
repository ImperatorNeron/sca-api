from dataclasses import dataclass

from fastapi import HTTPException, status

from app.schemas.missions import (
    CreateMissionWithTargetsSchema,
    ReadMissionWithTargetsSchema,
)
from app.services.missions import AbstractMissionService
from app.services.targets import AbstractTargetService
from app.utils.unit_of_work import AbstractUnitOfWork


@dataclass
class DeleteMissionUseCase:

    mission_service: AbstractMissionService

    async def execute(
        self,
        uow: AbstractUnitOfWork,
        mission_id: CreateMissionWithTargetsSchema,
    ) -> None:
        current_mission = await self.mission_service.get_mission(
            mission_id=mission_id,
            uow=uow,
        )

        if current_mission.spy_cat_id is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This mission has an associated spy cat and cannot be deleted.",
            )

        await self.mission_service.delete_mission(mission_id=mission_id, uow=uow)

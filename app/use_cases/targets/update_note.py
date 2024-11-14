from dataclasses import dataclass

from fastapi import HTTPException, status
from app.schemas.targets import ReadTargetSchema, UpdateTargetSchema
from app.services.missions import AbstractMissionService
from app.services.targets import AbstractTargetService
from app.utils.unit_of_work import AbstractUnitOfWork


@dataclass
class UpdateNoteUseCase:

    target_service: AbstractTargetService
    mission_service: AbstractMissionService

    async def execute(
        self,
        uow: AbstractUnitOfWork,
        target_in: UpdateTargetSchema,
        target_id: int,
        mission_id: int,
    ) -> ReadTargetSchema:

        current_mission = await self.mission_service.get_mission(
            mission_id=mission_id,
            uow=uow,
        )

        if current_mission.complete:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This mission has already been completed and cannot be updated.",
            )

        current_target = await self.target_service.get_target(
            target_id=target_id, uow=uow
        )

        if current_target.complete:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This target has already been completed and cannot be updated.",
            )

        return await self.target_service.update_target_notes(
            target_id=target_id,
            uow=uow,
            target_in=target_in,
        )

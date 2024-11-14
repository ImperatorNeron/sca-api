from dataclasses import dataclass

from fastapi import HTTPException, status

from app.schemas.missions import (
    CreateMissionSchema,
    CreateMissionWithTargetsSchema,
    ReadMissionSchema,
    ReadMissionWithTargetsSchema,
)
from app.services.missions import AbstractMissionService
from app.services.targets import AbstractTargetService
from app.utils.unit_of_work import AbstractUnitOfWork


@dataclass
class CreateMissionUseCase:

    mission_service: AbstractMissionService
    target_service: AbstractTargetService

    async def execute(
        self,
        uow: AbstractUnitOfWork,
        mission_in: CreateMissionWithTargetsSchema,
    ) -> ReadMissionWithTargetsSchema:
        async with uow:
            targets_len = len(mission_in.targets)
            if targets_len < 1 or len(mission_in.targets) > 3:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="The number of targets must be between 1 and 3.",
                )

            # TODO: add unique check

            mission: ReadMissionSchema = await self.mission_service.create_mission(
                uow=uow,
                mission_in=CreateMissionSchema(
                    **mission_in.model_dump(
                        exclude={"targets"},
                        exclude_unset=True,
                    )
                ),
            )

            targets = []
            for target in mission_in.targets:
                targets.append(
                    await self.target_service.create_target_to_mission(
                        uow=uow,
                        mission_id=mission.id,
                        target_in=target,
                    )
                )

            return ReadMissionWithTargetsSchema(**mission.model_dump(), targets=targets)

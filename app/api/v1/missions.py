from typing import Annotated
from fastapi import APIRouter, Depends
from punq import Container
from app.core.containers import get_container
from app.schemas.missions import (
    CreateMissionWithTargetsSchema,
    ReadMissionSchema,
    ReadMissionWithTargetsSchema,
)
from app.services.missions import AbstractMissionService
from app.use_cases.missions.create import CreateMissionUseCase
from app.use_cases.missions.delete import DeleteMissionUseCase
from app.utils.unit_of_work import AbstractUnitOfWork, UnitOfWork


router = APIRouter(prefix="/missions", tags=["Missions"])


@router.get("", response_model=list[ReadMissionWithTargetsSchema])
async def get_missions(
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractMissionService = container.resolve(AbstractMissionService)
    return await service.get_missions(uow=uow)


@router.get("/{mission_id}", response_model=ReadMissionSchema)
async def get_single_missions(
    mission_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractMissionService = container.resolve(AbstractMissionService)
    return await service.get_mission(uow=uow, mission_id=mission_id)


@router.post("", response_model=ReadMissionWithTargetsSchema)
async def create_mission(
    mission_in: CreateMissionWithTargetsSchema,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    use_case: CreateMissionUseCase = container.resolve(CreateMissionUseCase)
    return await use_case.execute(uow=uow, mission_in=mission_in)


@router.patch("/{mission_id}/spy-cat/{spy_cat_id}", response_model=ReadMissionSchema)
async def set_spy_cat_for_mission(
    mission_id: int,
    spy_cat_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractMissionService = container.resolve(AbstractMissionService)
    return await service.set_spy_cat_for_mission(
        uow=uow,
        mission_id=mission_id,
        spy_cat_id=spy_cat_id,
    )


@router.delete("/{mission_id}")
async def delete_mission(
    mission_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    user_case: DeleteMissionUseCase = container.resolve(DeleteMissionUseCase)
    return await user_case.execute(
        uow=uow,
        mission_id=mission_id,
    )

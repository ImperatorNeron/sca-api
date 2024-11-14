from typing import Annotated
from fastapi import APIRouter, Depends

from punq import Container
from app.core.containers import get_container
from app.schemas.targets import ReadTargetSchema, UpdateTargetSchema
from app.services.targets import AbstractTargetService
from app.use_cases.targets.update_note import UpdateNoteUseCase
from app.utils.unit_of_work import AbstractUnitOfWork, UnitOfWork


router = APIRouter(prefix="/targets", tags=["Targets"])


@router.get("/{mission_id}", response_model=list[ReadTargetSchema])
async def get_mission_targets(
    mission_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractTargetService = container.resolve(AbstractTargetService)
    return await service.get_mission_targets(uow=uow, mission_id=mission_id)


@router.patch("{mission_id}/target/{target_id}/update-note", response_model=ReadTargetSchema)
async def update_target_note(
    target_id: int,
    mission_id: int,
    target_in: UpdateTargetSchema,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    use_case: UpdateNoteUseCase = container.resolve(UpdateNoteUseCase)
    return await use_case.execute(
        uow=uow,
        target_id=target_id,
        target_in=target_in,
        mission_id=mission_id,
    )


@router.patch("/mark/{target_id}", response_model=ReadTargetSchema)
async def mark_target_complited(
    target_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractTargetService = container.resolve(AbstractTargetService)
    return await service.complite_target(
        uow=uow,
        target_id=target_id,
    )

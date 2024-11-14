from typing import Annotated
from fastapi import APIRouter, Depends

from app.core.containers import get_container
from punq import Container
from app.schemas.spy_cats import (
    CreateSpyCatSchema,
    ReadSpyCatSchema,
    UpdateSpyCatSchema,
)
from app.services.spy_cats import AbstractSpyCatService
from app.utils.unit_of_work import AbstractUnitOfWork, UnitOfWork


router = APIRouter(prefix="/spy-cats", tags=["SpyCats"])


@router.get("", response_model=list[ReadSpyCatSchema])
async def get_spy_cats(
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractSpyCatService = container.resolve(AbstractSpyCatService)
    return await service.get_spy_cats(uow=uow)


@router.get("/{spy_cat_id}", response_model=ReadSpyCatSchema)
async def get_single_spy_cat(
    spy_cat_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractSpyCatService = container.resolve(AbstractSpyCatService)
    return await service.get_single_spy_cat(uow=uow, spy_cat_id=spy_cat_id)


@router.post("", response_model=ReadSpyCatSchema)
async def create_spy_cat(
    spy_cat_in: CreateSpyCatSchema,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractSpyCatService = container.resolve(AbstractSpyCatService)
    return await service.create_spy_cat(uow=uow, spy_cat_in=spy_cat_in)


@router.patch("/{spy_cat_id}", response_model=ReadSpyCatSchema)
async def update_spy_cat(
    spy_cat_id: int,
    spy_cat_in: UpdateSpyCatSchema,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractSpyCatService = container.resolve(AbstractSpyCatService)
    return await service.update_spy_cat(
        uow=uow,
        spy_cat_id=spy_cat_id,
        spy_cat_in=spy_cat_in,
    )


@router.delete("/{spy_cat_id}", response_model=None)
async def delete_spy_cat(
    spy_cat_id: int,
    container: Annotated[Container, Depends(get_container)],
    uow: Annotated[AbstractUnitOfWork, Depends(UnitOfWork)],
):
    service: AbstractSpyCatService = container.resolve(AbstractSpyCatService)
    return await service.delete_single_spy_cat(uow=uow, spy_cat_id=spy_cat_id)

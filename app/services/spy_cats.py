from abc import ABC, abstractmethod

from app.schemas.spy_cats import (
    CreateSpyCatSchema,
    ReadSpyCatSchema,
    UpdateSpyCatSchema,
)
from app.utils.unit_of_work import AbstractUnitOfWork


class AbstractSpyCatService(ABC):

    @abstractmethod
    async def get_spy_cats(
        self,
        uow: AbstractUnitOfWork,
    ) -> list[ReadSpyCatSchema]: ...

    @abstractmethod
    async def get_single_spy_cat(
        self, uow: AbstractUnitOfWork, spy_cat_id: int
    ) -> ReadSpyCatSchema: ...

    @abstractmethod
    async def create_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_in: CreateSpyCatSchema,
    ) -> ReadSpyCatSchema: ...

    @abstractmethod
    async def update_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_id: int,
        spy_cat_in: UpdateSpyCatSchema,
    ) -> ReadSpyCatSchema: ...

    @abstractmethod
    async def delete_single_spy_cat(
        self, uow: AbstractUnitOfWork, spy_cat_id: int
    ) -> None: ...


class SpyCatService(AbstractSpyCatService):

    async def get_spy_cats(
        self,
        uow: AbstractUnitOfWork,
    ) -> list[ReadSpyCatSchema]:
        async with uow:
            return await uow.spy_cats.fetch_all()

    async def get_single_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_id: int,
    ) -> ReadSpyCatSchema:
        async with uow:
            return await uow.spy_cats.fetch_by_id(item_id=spy_cat_id)

    async def create_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_in: CreateSpyCatSchema,
    ) -> list[ReadSpyCatSchema]:
        async with uow:
            return await uow.spy_cats.create(item_in=spy_cat_in)

    async def update_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_id: int,
        spy_cat_in: UpdateSpyCatSchema,
    ) -> ReadSpyCatSchema:
        async with uow:
            return await uow.spy_cats.update_by_id(
                item_id=spy_cat_id,
                item_in=spy_cat_in,
            )

    async def delete_single_spy_cat(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_id: int,
    ) -> None:
        async with uow:
            return await uow.spy_cats.remove_by_id(item_id=spy_cat_id)

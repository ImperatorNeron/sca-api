from abc import ABC, abstractmethod

from app.schemas.targets import (
    CreateTargetForMissionSchema,
    CreateTargetSchema,
    ReadTargetSchema,
    UpdateTargetCompletionStatusSchema,
    UpdateTargetSchema,
)
from app.utils.unit_of_work import AbstractUnitOfWork


class AbstractTargetService(ABC):

    @abstractmethod
    async def get_target(
        self,
        target_id: int,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema: ...

    @abstractmethod
    async def get_mission_targets(
        self,
        mission_id: int,
        uow: AbstractUnitOfWork,
    ) -> list[ReadTargetSchema]: ...

    @abstractmethod
    async def create_target_to_mission(
        self,
        mission_id: int,
        target_in: CreateTargetSchema,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema: ...

    @abstractmethod
    async def update_target_notes(
        self,
        target_id: int,
        target_in: UpdateTargetSchema,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema: ...

    @abstractmethod
    async def complite_target(
        self,
        target_id: int,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema: ...


class TargetService(AbstractTargetService):

    async def get_target(
        self,
        target_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            return await uow.targets.fetch_by_id(item_id=target_id)

    async def create_target_to_mission(
        self,
        mission_id: int,
        target_in: CreateTargetSchema,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema:
        return await uow.targets.create(
            item_in=CreateTargetForMissionSchema(
                **target_in.model_dump(),
                mission_id=mission_id,
            )
        )

    async def get_mission_targets(
        self,
        mission_id: int,
        uow: AbstractUnitOfWork,
    ):
        async with uow:
            return await uow.targets.fetch_by_attributes(mission_id=mission_id)

    async def update_target_notes(
        self,
        target_id: int,
        target_in: UpdateTargetSchema,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema:
        async with uow:
            return await uow.targets.update_by_id(
                item_id=target_id,
                item_in=target_in,
            )

    async def complite_target(
        self,
        target_id: int,
        uow: AbstractUnitOfWork,
    ) -> ReadTargetSchema:
        async with uow:
            return await uow.targets.update_by_id(
                item_id=target_id,
                item_in=UpdateTargetCompletionStatusSchema(complete=True),
            )

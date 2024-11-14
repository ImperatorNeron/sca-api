from abc import ABC, abstractmethod

from app.schemas.missions import (
    CreateMissionSchema,
    ReadMissionSchema,
    ReadMissionWithTargetsSchema,
    UpdateMissionSchema,
)
from app.utils.unit_of_work import AbstractUnitOfWork


class AbstractMissionService(ABC):

    @abstractmethod
    async def get_missions(
        self,
        uow: AbstractUnitOfWork,
    ) -> ReadMissionWithTargetsSchema: ...

    @abstractmethod
    async def get_mission(
        self,
        mission_id: int,
        uow: AbstractUnitOfWork,
    ) -> ReadMissionSchema: ...

    @abstractmethod
    async def create_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_in: CreateMissionSchema,
    ) -> ReadMissionSchema: ...

    @abstractmethod
    async def set_spy_cat_for_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_id: int,
        spy_cat_id: int,
    ) -> ReadMissionSchema: ...

    @abstractmethod
    async def delete_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_id: int,
    ) -> ReadMissionSchema: ...


class MissionService(AbstractMissionService):

    async def create_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_in: CreateMissionSchema,
    ) -> ReadMissionSchema:
        return await uow.missions.create(item_in=mission_in)

    async def get_missions(
        self,
        uow: AbstractUnitOfWork,
    ) -> list[ReadMissionWithTargetsSchema]:
        async with uow:
            return await uow.missions.get_missions_with_targets()

    async def get_mission(
        self,
        mission_id: int,
        uow: AbstractUnitOfWork,
    ) -> ReadMissionSchema:
        async with uow:
            return await uow.missions.fetch_by_id(mission_id)

    async def set_spy_cat_for_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_id: int,
        spy_cat_id: int,
    ) -> ReadMissionSchema:
        async with uow:
            return await uow.missions.update_by_id(
                item_id=mission_id,
                item_in=UpdateMissionSchema(
                    spy_cat_id=spy_cat_id,
                ),
            )

    async def delete_mission(
        self,
        uow: AbstractUnitOfWork,
        mission_id: int,
    ) -> ReadMissionSchema:
        async with uow:
            await uow.missions.remove_by_id(item_id=mission_id)

from abc import (
    ABC,
    abstractmethod,
)
from typing import Type

from app.db.db import database_helper
from app.repositories.spy_cats import SpyCatRepository


class AbstractUnitOfWork(ABC):
    """Abstract base class defining a unit of work pattern for managing
    repositories and database transactions."""

    spy_cats: Type[SpyCatRepository]

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class BaseUnitOfWork(AbstractUnitOfWork):
    async def __aenter__(self):
        self.session = await self._get_session()
        self.spy_cats = SpyCatRepository(session=self.session)
        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    @abstractmethod
    async def _get_session(self): ...


class UnitOfWork(BaseUnitOfWork):
    """Implementation of the UnitOfWork pattern."""

    async def _get_session(self):
        return database_helper.session_factory()

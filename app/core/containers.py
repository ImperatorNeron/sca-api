from functools import lru_cache

import punq

from app.services.missions import AbstractMissionService, MissionService
from app.services.spy_cats import AbstractSpyCatService, SpyCatService
from app.services.targets import AbstractTargetService, TargetService
from app.use_cases.missions.create import CreateMissionUseCase
from app.use_cases.missions.delete import DeleteMissionUseCase
from app.use_cases.spy_cats.create import CreateSpyCatUseCase
from app.use_cases.targets.update_note import UpdateNoteUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # Services
    container.register(AbstractSpyCatService, SpyCatService)
    container.register(AbstractMissionService, MissionService)
    container.register(AbstractTargetService, TargetService)

    # UseCases
    container.register(CreateSpyCatUseCase)
    container.register(CreateMissionUseCase)
    container.register(UpdateNoteUseCase)
    container.register(DeleteMissionUseCase)
    return container

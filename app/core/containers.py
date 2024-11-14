from functools import lru_cache

import punq

from app.services.spy_cats import AbstractSpyCatService, SpyCatService
from app.use_cases.spy_cats.create import CreateSpyCatUseCase


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # Services
    container.register(AbstractSpyCatService, SpyCatService)

    # UseCases
    container.register(CreateSpyCatUseCase)
    return container

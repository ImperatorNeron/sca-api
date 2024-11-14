from dataclasses import dataclass

from fastapi import HTTPException, status
import requests
from app.schemas.spy_cats import CreateSpyCatSchema, ReadSpyCatSchema
from app.services.spy_cats import AbstractSpyCatService
from app.utils.unit_of_work import AbstractUnitOfWork


@dataclass
class CreateSpyCatUseCase:

    spy_cats_service: AbstractSpyCatService

    async def __do_request(self) -> list:
        api_url = "https://api.thecatapi.com/v1/breeds"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            return [cat["name"] for cat in data]

        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"API request failed: {e}",
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Data error: {e}",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get cat breeds: {e}",
            )

    async def execute(
        self,
        uow: AbstractUnitOfWork,
        spy_cat_in: CreateSpyCatSchema,
    ) -> ReadSpyCatSchema:
        breeds = await self.__do_request()
        if spy_cat_in.breed in breeds:
            return await self.spy_cats_service.create_spy_cat(
                uow=uow, spy_cat_in=spy_cat_in
            )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No cat breed could be found in the API response.",
        )

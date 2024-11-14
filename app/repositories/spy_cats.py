from app.models.spy_cats import SpyCats
from app.utils.sql_repository import SQLAlchemyRepository


class SpyCatRepository(SQLAlchemyRepository):

    model = SpyCats

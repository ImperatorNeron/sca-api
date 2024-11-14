from app.models.spy_cats import SpyCat
from app.utils.sql_repository import SQLAlchemyRepository


class SpyCatRepository(SQLAlchemyRepository):

    model = SpyCat

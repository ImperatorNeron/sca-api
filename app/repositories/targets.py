from app.models.targets import Target
from app.utils.sql_repository import SQLAlchemyRepository


class TargetRepository(SQLAlchemyRepository):

    model = Target

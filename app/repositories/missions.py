from collections import defaultdict
from sqlalchemy import select
from app.models.missions import Mission
from app.schemas.missions import ReadMissionWithTargetsSchema
from app.utils.sql_repository import SQLAlchemyRepository
from sqlalchemy.orm import joinedload


class MissionRepository(SQLAlchemyRepository):

    model = Mission

    async def get_missions_with_targets(self):
        result = await self.session.execute(
            select(Mission).options(joinedload(Mission.targets))
        )
        missions = result.scalars().all()
        full_missions = defaultdict(list)

        for mission in missions:
            full_missions[mission].append(mission.targets)

        return [
            ReadMissionWithTargetsSchema(
                **mission.to_read_model().model_dump(),
                targets=[target.to_read_model() for target in targets]
            )
            for mission, targets in full_missions.items()
        ]

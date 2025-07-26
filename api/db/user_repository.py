from sqlalchemy import select

from api.db.base_database_repository import BaseDatabaseRepository
from api.db.error_handlers import handle_db_error
from api.models.users import User


class UserDatabaseRepository(BaseDatabaseRepository):
    model_class = User

    @handle_db_error
    async def read_one_or_none(self, username: str):
        query = select(self.model_class).where(self.model_class.username == username)
        result = await self.session.execute(query)
        user = result.scalars().one_or_none()
        if not user:
            return None
        return user

    @handle_db_error
    async def read_one_or_none_by_id(self, user_id: int):
        query = select(self.model_class).where(self.model_class.id == user_id)
        result = await self.session.execute(query)
        user = result.scalars().one_or_none()
        if not user:
            return None
        return user

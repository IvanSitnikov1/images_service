from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from api.db.image_repository import ImageDatabaseRepository, ProcessedImageDatabaseRepository


async def get_image_repo(session: AsyncSession = Depends(get_async_session)):
    yield ImageDatabaseRepository(session)


async def get_processed_image_repo(session: AsyncSession = Depends(get_async_session)):
    yield ProcessedImageDatabaseRepository(session)

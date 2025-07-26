from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.DTO.endpoints.images.read_image_dto import ImagesReadResponseDTO, ImageReadDTO
from api.configs.dependensies import get_current_user
from api.configs.get_obj_db import get_image_repo
from api.db.image_repository import ImageDatabaseRepository
from api.models.users import User


async def get_images(
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
    _: User = Depends(get_current_user),
):
    model = image_repo.model_class
    query = select(model).options(selectinload(model.processed_images))
    images = await image_repo.read_all(query)
    return ImagesReadResponseDTO(
        detail='Изображения получены успешно',
        data=[ImageReadDTO.model_validate(image) for image in images]
    )

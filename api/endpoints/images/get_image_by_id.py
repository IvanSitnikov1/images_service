from fastapi import Depends
from sqlalchemy.orm import selectinload

from api.DTO.endpoints.images.read_image_dto import ImageReadResponseDTO, ImageReadDTO
from api.configs.dependensies import get_current_user
from api.configs.get_obj_db import get_image_repo
from api.db.image_repository import ImageDatabaseRepository
from api.models.users import User


async def get_image_by_id(
    image_id: int,
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
    _: User = Depends(get_current_user),
):
    model = image_repo.model_class
    image = await image_repo.read_by_id(image_id, [selectinload(model.processed_images)])
    return ImageReadResponseDTO(
        detail='Изображение получено успешно',
        data=ImageReadDTO.model_validate(image)
    )

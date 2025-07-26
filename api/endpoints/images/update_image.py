from fastapi import Depends

from api.DTO.endpoints.images.update_image import ImageUpdateReadResponseDTO, ImageUpdateReadDTO
from api.configs.dependensies import get_current_admin_user
from api.configs.get_obj_db import get_image_repo
from api.db.image_repository import ImageDatabaseRepository
from api.models.users import User


async def update_image(
    image_id: int,
    image_name: str,
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
    _: User = Depends(get_current_admin_user),
):
    updated_data = {"name": image_name}
    updated_image = await image_repo.update(image_id, updated_data)
    return ImageUpdateReadResponseDTO(
        detail='Название изображения изменено успешно',
        data=ImageUpdateReadDTO.model_validate(updated_image)
    )

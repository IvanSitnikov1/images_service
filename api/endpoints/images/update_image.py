from fastapi import Depends

from api.DTO.endpoints.images.read_image_dto import ImageReadResponseDTO, ImageReadDTO
from api.configs.get_obj_db import get_image_repo
from api.db.image_repository import ImageDatabaseRepository


async def update_image(
    image_id: int,
    image_name: str,
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
):
    updated_data = {"name": image_name}
    updated_image = await image_repo.update(image_id, updated_data)
    return ImageReadResponseDTO(
        detail='Название изображения изменено успешно',
        data=ImageReadDTO.model_validate(updated_image)
    )

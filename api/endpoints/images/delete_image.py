import os
import shutil

from fastapi import Depends

from api.configs.settings import settings
from api.configs.get_obj_db import get_image_repo
from api.db.image_repository import ImageDatabaseRepository


async def delete_image(
    image_id: int,
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
):
    image = await image_repo.read_by_id(image_id)

    original_path = os.path.join(settings.STATIC_PATH, image.name)
    processed_dir = os.path.join(settings.STATIC_PATH, image.name.split('.')[0])
    # Удаление оригинального изображения
    if os.path.exists(original_path):
        os.remove(original_path)
    # Удаление папки с дополнительными изображениями
    if os.path.exists(processed_dir) and os.path.isdir(processed_dir):
        shutil.rmtree(processed_dir)

    await image_repo.delete(image_id)
    return

import os

from fastapi import UploadFile, File, HTTPException, Depends
from PIL import Image as PilImage

from api.DTO.endpoints.images.image_upload_dto import ImageUploadDTO
from api.configs.get_obj_db import get_image_repo, get_processed_image_repo
from api.configs.settings import settings
from api.db.image_repository import ImageDatabaseRepository, ProcessedImageDatabaseRepository


async def upload_image(
    file_image: UploadFile = File(...),
    image_repo: ImageDatabaseRepository = Depends(get_image_repo),
    processed_image_repo: ProcessedImageDatabaseRepository = Depends(get_processed_image_repo)
):
    if not file_image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail=f"Файл должен быть изображением")

    original_image = PilImage.open(file_image.file)
    width, height = original_image.size

    # Сохраняем оригинал
    original_image_path = f"{settings.STATIC_PATH}/{file_image.filename}"
    original_image.save(original_image_path)
    file_size_kb = os.path.getsize(original_image_path) / 1024 # байты

    new_image_data = {
        'name': file_image.filename,
        'file_path': original_image_path,
        'resolution': f'{width}x{height}',
        'file_size': file_size_kb,
        'format': file_image.content_type.split('/')[1],
    }
    new_image = await image_repo.create(new_image_data)

    processed_dir_name = new_image.name.split('.')[0]
    os.makedirs(f"{settings.STATIC_PATH}/{processed_dir_name}", exist_ok=True)

    gray_image = original_image.convert('L')
    gray_path = f'{settings.STATIC_PATH}/{processed_dir_name}/gray_{new_image.name}'
    gray_image.save(gray_path)

    processed_image_data = {
        'file_path': gray_path,
        'resolution': new_image.resolution,
        'original_image': new_image,
    }
    await processed_image_repo.create(processed_image_data)

    sizes = [(100, 100), (500, 500)]
    for width, height in sizes:
        # Принудительное изменение размера без сохранения пропорций
        resized_image = original_image.resize((width, height), PilImage.Resampling.LANCZOS)
        # Генерация имени и пути
        resolution = f'{width}x{height}'
        resized_filename = f"{resolution}_{file_image.filename}"
        resized_path = f"{settings.STATIC_PATH}/{processed_dir_name}/{resized_filename}"
        resized_image.save(resized_path)

        processed_image_data = {
            'file_path': resized_path,
            'resolution': resolution,
            'original_image': new_image,
        }
        await processed_image_repo.create(processed_image_data)

    return ImageUploadDTO(
        detail='Изображение загружено успешно',
        image_id=new_image.id,
    )

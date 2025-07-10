from fastapi import status

from api.DTO.endpoints.images.image_upload_dto import ImageUploadDTO
from api.DTO.endpoints.images.read_image_dto import ImagesReadResponseDTO, ImageReadResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.images.delete_image import delete_image
from api.endpoints.images.get_image_by_id import get_image_by_id
from api.endpoints.images.get_images import get_images
from api.endpoints.images.update_image import update_image
from api.endpoints.images.upload_image import upload_image


IMAGES_ROUTES = [
    RouteDTO(
        path="/",
        endpoint=upload_image,
        response_model=ImageUploadDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
        summary="Загрузка изображения",
        description="""
        Эндпоинт принимает изображение из формы, сохраняет его на сервере и в базе данных""",
        responses={
            status.HTTP_201_CREATED: {
                "description": "Изображение загружено успешно",
            },
        },
    ),
    RouteDTO(
        path="/",
        endpoint=get_images,
        response_model=ImagesReadResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получение всех изображений",
        description="""
        Эндпоинт получает список всех изображений и выводит их данные
        """,
        responses={
            status.HTTP_200_OK: {
                "description": "Изображения получены успешно",
            },
        },
    ),
    RouteDTO(
        path="/{image_id}",
        endpoint=get_image_by_id,
        response_model=ImageReadResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Получение изображения",
        description="""
        Эндпоинт получает конкретное изображение по id и выводит его данные
        """,
        responses={
            status.HTTP_200_OK: {
                "description": "Изображение получено успешно",
            },
        },
    ),
    RouteDTO(
        path="/{image_id}",
        endpoint=update_image,
        response_model=ImageReadResponseDTO,
        methods=["PATCH"],
        status_code=status.HTTP_200_OK,
        summary="Редактирование названия изображения",
        description="""
        Эндпоинт редактирует название изображения
        """,
        responses={
            status.HTTP_200_OK: {
                "description": "Название изображения изменено успешно",
            },
        },
    ),
    RouteDTO(
        path="/{image_id}",
        endpoint=delete_image,
        response_model=None,
        methods=["PATCH"],
        status_code=status.HTTP_204_NO_CONTENT,
        summary="Удаление изображения",
        description="""
        Эндпоинт удаляет изображение по id с сервера и из базы данных
        """,
        responses={
            status.HTTP_204_NO_CONTENT: {
                "description": "Изображение удалено успешно",
            },
        },
    ),
]

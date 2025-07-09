from fastapi import status

from api.DTO.endpoints.images.image_upload_dto import ImageUploadDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.images.upload_image import upload_image

IMAGES_ROUTES = [
    RouteDTO(
        path="/upload",
        endpoint=upload_image,
        response_model=ImageUploadDTO,
        methods=["POST"],
        status_code=201,
        summary="Загрузка изображения",
        description="""
        Эндпоинт принимает изображение из формы, сохраняет его на сервере и в базе данных""",
        responses={
            # status.HTTP_201_CREATED: {
            #     "description": "Проект создан успешно",
            # },
            # status.HTTP_409_CONFLICT: {
            #     "description": "Нарушение уникальности при создании проекта",
            #     "content": {
            #         "application/json": {
            #             "example": {"detail": "Некорректные данные в запросе"}
            #         }
            #     },
            # },
        },
    ),
]
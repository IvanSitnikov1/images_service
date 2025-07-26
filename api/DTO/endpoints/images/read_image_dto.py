from datetime import date

from pydantic import BaseModel, ConfigDict


class ProcessedImageReadDTO(BaseModel):
    id: int
    file_path: str
    resolution: str
    is_grayscale: bool

    model_config = ConfigDict(from_attributes=True)


class ImageReadDTO(BaseModel):
    id: int
    name: str
    file_path: str
    upload_date: date
    resolution: str
    file_size: int
    format: str
    processed_images: list[ProcessedImageReadDTO]

    model_config = ConfigDict(from_attributes=True)


class ImagesReadResponseDTO(BaseModel):
    detail: str
    data: list[ImageReadDTO]


class ImageReadResponseDTO(BaseModel):
    detail: str
    data: ImageReadDTO

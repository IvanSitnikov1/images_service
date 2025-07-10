from datetime import date

from pydantic import BaseModel


class ProcessedImageReadDTO(BaseModel):
    id: int
    file_path: str
    resolution: str
    is_grayscale: bool


class ImageReadDTO(BaseModel):
    id: int
    name: str
    file_path: str
    upload_date: date
    resolution: str
    file_size: int
    format: str
    processed_images: list[ProcessedImageReadDTO]


class ImagesReadResponseDTO(BaseModel):
    detail: str
    data: list[ImageReadDTO]


class ImageReadResponseDTO(BaseModel):
    detail: str
    data: ImageReadDTO

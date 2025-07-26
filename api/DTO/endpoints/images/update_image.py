from datetime import date

from pydantic import BaseModel, ConfigDict


class ImageUpdateReadDTO(BaseModel):
    id: int
    name: str
    file_path: str
    upload_date: date
    resolution: str
    file_size: int
    format: str

    model_config = ConfigDict(from_attributes=True)


class ImageUpdateReadResponseDTO(BaseModel):
    detail: str
    data: ImageUpdateReadDTO

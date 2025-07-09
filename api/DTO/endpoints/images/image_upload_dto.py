from pydantic import BaseModel


class ImageUploadDTO(BaseModel):
    detail: str
    image_id: int

from pydantic import BaseModel


class LogoutResponseDTO(BaseModel):
    detail: str

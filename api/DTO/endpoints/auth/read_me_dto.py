from pydantic import BaseModel


class MeReadResponseDTO(BaseModel):
    id: int
    username: str
    hashed_password: str
    is_user: bool
    is_admin: bool

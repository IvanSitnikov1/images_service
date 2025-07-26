from pydantic import BaseModel


class UserRegisterDTO(BaseModel):
    username: str
    password: str


class UserRegisterReadDTO(BaseModel):
    username: str
    hashed_password: str


class UserRegisterResponseDTO(BaseModel):
    detail: str
    data: UserRegisterReadDTO

from pydantic import BaseModel


class LoginDTO(BaseModel):
    username: str
    password:str


class LoginDataResponseDTO(BaseModel):
    access_token: str
    refresh_token: str | None


class LoginResponseDTO(BaseModel):
    detail: str
    data: LoginDataResponseDTO

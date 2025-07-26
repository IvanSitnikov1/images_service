from fastapi import Depends

from api.DTO.endpoints.auth.read_me_dto import MeReadResponseDTO
from api.configs.dependensies import get_current_user
from api.models.users import User


async def get_me(user_data: User = Depends(get_current_user)):
    return MeReadResponseDTO.model_validate(user_data, from_attributes=True)

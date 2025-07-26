from fastapi import Depends

from api.DTO.endpoints.auth.register_dto import (
    UserRegisterDTO,
    UserRegisterResponseDTO,
    UserRegisterReadDTO,
)
from api.configs.get_obj_db import get_user_repo
from api.db.user_repository import UserDatabaseRepository
from api.utils.auth.auth_utils import get_password_hash


async def register(
    new_user_data: UserRegisterDTO,
    user_repo: UserDatabaseRepository = Depends(get_user_repo),
):
    new_user_dict = {
        'username': new_user_data.username,
        'hashed_password': await get_password_hash(new_user_data.password)
    }
    new_user = await user_repo.create(new_user_dict)

    return UserRegisterResponseDTO(
        detail='Пользователь зарегистрирован успешно',
        data=UserRegisterReadDTO(
            username=new_user.username,
            hashed_password=new_user.hashed_password,
        ),
    )

from fastapi import Depends, HTTPException, Response

from api.DTO.endpoints.auth.login_dto import LoginDTO, LoginResponseDTO, LoginDataResponseDTO
from api.configs.get_obj_db import get_user_repo
from api.db.user_repository import UserDatabaseRepository
from api.utils.auth.auth_utils import verify_password, create_access_token


async def login(
    response: Response,
    login_data: LoginDTO,
    user_repo: UserDatabaseRepository = Depends(get_user_repo),
):
    exists_user = await user_repo.read_one_or_none(login_data.username)
    if not exists_user or not await verify_password(login_data.password, exists_user.hashed_password):
        raise HTTPException(401, 'Неверный логин или пароль')

    access_token = await create_access_token({"sub": str(exists_user.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return LoginResponseDTO(
        detail='Пользователь успешно аутентифицирован',
        data=LoginDataResponseDTO(
            access_token=access_token,
            refresh_token=None,
        )
    )

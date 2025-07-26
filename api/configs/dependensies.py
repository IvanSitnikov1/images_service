from fastapi import HTTPException, Depends
from fastapi.security import APIKeyCookie
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError

from api.configs.get_obj_db import get_user_repo
from api.configs.settings import settings
from api.db.user_repository import UserDatabaseRepository
from api.models.users import User


cookie_scheme = APIKeyCookie(name="users_access_token", auto_error=True)


async def get_current_user(
    token: str = Depends(cookie_scheme),
    user_repo: UserDatabaseRepository = Depends(get_user_repo),
) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise HTTPException(401, 'Токен просрочен')
    except JWTError:
        raise HTTPException(401, 'Токен не валидный')

    user_id = payload.get('sub')
    user = await user_repo.read_one_or_none_by_id(int(user_id))
    if not user:
        raise HTTPException(401, 'Пользователь токена не найден')

    return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_admin:
        raise HTTPException(403, 'Недостаточно прав, пользователь не администратор')
    return current_user

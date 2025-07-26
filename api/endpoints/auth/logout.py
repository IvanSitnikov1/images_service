from fastapi import Response

from api.DTO.endpoints.auth.logout_dto import LogoutResponseDTO


async def logout(response: Response):
    response.delete_cookie('users_access_token')
    return LogoutResponseDTO(
        detail='Пользователь вышел из системы, куки очищены',
    )

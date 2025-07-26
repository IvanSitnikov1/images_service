from fastapi import status

from api.DTO.endpoints.auth.login_dto import LoginResponseDTO
from api.DTO.endpoints.auth.logout_dto import LogoutResponseDTO
from api.DTO.endpoints.auth.read_me_dto import MeReadResponseDTO
from api.DTO.endpoints.auth.register_dto import UserRegisterResponseDTO
from api.DTO.factories.router_factory import RouteDTO
from api.endpoints.auth.get_me import get_me
from api.endpoints.auth.login import login
from api.endpoints.auth.logout import logout
from api.endpoints.auth.register import register


AUTH_ROUTES = [
    RouteDTO(
        path="/register",
        endpoint=register,
        response_model=UserRegisterResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_201_CREATED,
        summary="",
        description="""
        
        """,
        responses={
            status.HTTP_201_CREATED: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/login",
        endpoint=login,
        response_model=LoginResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="""

        """,
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/me",
        endpoint=get_me,
        response_model=MeReadResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="""

        """,
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
    RouteDTO(
        path="/logout",
        endpoint=logout,
        response_model=LogoutResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="",
        description="""

        """,
        responses={
            status.HTTP_200_OK: {
                "description": "",
            },
        },
    ),
]

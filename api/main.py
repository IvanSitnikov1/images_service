from api.configs.app import app
from api.router_factory import RouterFactory
from api.routes.images_routes import IMAGES_ROUTES
from api.routes.auth_routes import AUTH_ROUTES


image_router = RouterFactory(prefix='/api/v1/images', tags=['Изображения'], routes=IMAGES_ROUTES)
app.include_router(image_router())

auth_router = RouterFactory(prefix='/auth', tags=['Аутентификация'], routes=AUTH_ROUTES)
app.include_router(auth_router())

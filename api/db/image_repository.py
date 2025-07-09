from api.db.base_database_repository import BaseDatabaseRepository
from api.models.images import Image, ProcessedImage


class ImageDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с базой данных изображений."""
    model_class = Image


class ProcessedImageDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с базой данных дополнительных изображений."""
    model_class = ProcessedImage

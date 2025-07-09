import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger("Системный")
logger.setLevel(logging.DEBUG)

# Настраиваем форматтер
formatter = logging.Formatter(
    fmt="[{asctime}] [{levelname:^8}] [{name}] {message}",
    datefmt="%Y-%m-%d %H:%M:%S",
    style="{",
)

# Настройка для файла
file_handler = RotatingFileHandler(
    "api/log/api.log", maxBytes=5 * 1024 * 1024, backupCount=1, encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Настройка для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# добавление обработчика к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

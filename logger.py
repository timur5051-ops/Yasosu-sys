import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app_debug.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logger()

def log_error(error_message, module_name=""):
    logger.error(f"Модуль {module_name}: {error_message}")

def log_info(info_message, module_name=""):
    logger.info(f"Модуль {module_name}: {info_message}")

def log_debug(debug_message, module_name=""):
    logger.debug(f"Модуль {module_name}: {debug_message}")

if __name__ == "__main__":
    log_info("Логгер инициализирован", "logger")
    log_error("Тестовая ошибка", "logger")
    print("Логгер создан. Логи будут в файле app_debug.log")
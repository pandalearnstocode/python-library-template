import os
from loguru import logger
from lib_template.settings import LOG_DIR

log_path = os.path.join(LOG_DIR, "sub_module_2.log")
logger.add(log_path, level="DEBUG")


def hello_mcu():
    print("Hello MCU inside print!")
    logger.info("Hello MCU inside log!")
    return "Hello MCU!"

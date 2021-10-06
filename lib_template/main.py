import os
import pathlib
from loguru import logger
from lib_template import sub_module_1
from lib_template import sub_module_2
from lib_template.settings import LOG_DIR

log_path = pathlib.Path(os.path.join(LOG_DIR, "main.log"))
logger.add(log_path, level="DEBUG")


def say_hello(type_of_greeting):
    if type_of_greeting == "hello":
        logger.info("Hello")
        result = sub_module_1.hello_world()
    else:
        logger.info("MCU")
        result = sub_module_2.hello_mcu()
    return result

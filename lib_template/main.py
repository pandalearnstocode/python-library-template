import os
from loguru import logger
import lib_template.sub_module_1 as sub_module_1
import lib_template.sub_module_2 as sub_module_2
from lib_template.settings import LOG_DIR
log_path = os.path.join(LOG_DIR, "main.log")
logger.add(log_path, level='DEBUG')


def say_hello(type_of_greeting):
    if type_of_greeting == "hello":
        logger.info("Hello")
        return sub_module_1.hello_world()
    else:
        logger.info("MCU")
        return sub_module_2.hello_mcu()

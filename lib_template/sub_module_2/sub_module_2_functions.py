from loguru import logger
import os
from lib_template.settings import log_dir
log_path = os.path.join(log_dir, "sub_module_2.log")
logger.add(log_path, level='DEBUG')

def hello_mcu():
    print("Hello MCU inside print!")
    logger.info("Hello MCU inside log!")
    return "Hello MCU!"

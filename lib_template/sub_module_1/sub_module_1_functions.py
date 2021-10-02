import os
from loguru import logger
from lib_template.settings import log_dir
log_path = os.path.join(log_dir, "sub_module_1.log")
logger.add(log_path, level='DEBUG')

def hello_world():
    print("Hello World inside print!")
    logger.info("Hello World inside log!")
    return "Hello World!"

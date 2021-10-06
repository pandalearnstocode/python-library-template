# LOG_DIR, and DATA_DIR are two folder which will be present in the working directory
# if there are not present the path has to be suppied as env variables and in settings.py
# these has to be read and used in further application.
# It should not be hard coded. Also, the should be an option to pass it from high level API and env
# variables.

import os
from loguru import logger
from lib_template.settings import LOG_DIR

log_path = os.path.join(LOG_DIR, "sub_module_1.log")
logger.add(log_path, level="DEBUG")


def hello_world():
    print("Hello World inside print!")
    logger.info("Hello World inside log!")
    return "Hello World!"

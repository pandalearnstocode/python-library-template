# These are the settings which can be made available in 3 ways.
# user input: a user should be able to supplied these values as args.
# default value: current working directory + logs or data.
# env variables: it can be supplied as env variables.
# If these values are not available by above three methods raise error and stop the process which is
# integrating with these.
import os
import pathlib
from dotenv import load_dotenv
from loguru import logger
load_dotenv()
LOG_DIR = "logs"
DATA_DIR = "data"
LOG_DIR_LOCAL = "lib_template/logs"
DATA_DIR_LOCAL = "lib_template/data"
try:
    LOG_DIR = pathlib.Path(os.getenv("LOG_DIR"))
    DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))
    logger.info("Assigning values to LOG_DIR and DATA_DIR from env variable.")
except Exception as e:
    try:
        if not LOG_DIR.is_dir():
            LOG_DIR = LOG_DIR_LOCAL
        if not DATA_DIR.is_dir():
            DATA_DIR = DATA_DIR_LOCAL
    except Exception as e:
        logger.error(f"Error in assigning values to LOG_DIR and DATA_DIR from env variable. {e}")
        raise e

logger.info(f"Logging will be stored in : {LOG_DIR}.")
logger.info(f"Data will be stored in : {DATA_DIR}.")


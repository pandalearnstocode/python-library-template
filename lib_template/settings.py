# These are the settings which can be made available in 3 ways.
# user input: a user should be able to supplied these values as args.
# default value: current working directory + logs or data.
# env variables: it can be supplied as env variables.
# If these values are not available by above three methods raise error and stop the process which is
# integrating with these.
import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

LOG_DIR = pathlib.Path(os.getenv("LOG_DIR"))
DATA_DIR = pathlib.Path(os.getenv("DATA_DIR"))
LOG_DIR_LOCAL = "lib_template/logs"
DATA_DIR = "lib_template/data"
if not LOG_DIR.is_dir():
    LOG_DIR = LOG_DIR_LOCAL
if not DATA_DIR.is_dir():
    DATA_DIR = DATA_DIR
from logging import getLogger, basicConfig, INFO, DEBUG, FileHandler

# file handler setup:
file_handler = FileHandler("data.log")
file_handler.setLevel(DEBUG)

# logger setup:
logger = getLogger(__name__)
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'

# DIWEC (уровни) : DEBUG < INFO < WARNING < ERROR < CRITICAL
basicConfig(level=DEBUG, format=FORMAT, handlers=[file_handler]) 

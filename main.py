import os
from logging import Logger
from LoggerHandler import LoggerHandler
from LoggingType import LoggingType

if __name__ == "__main__":
    LoggerHandler.setup_logging()
    os.mkdir("src")
    LoggerHandler.log(__name__,LoggingType.INFO, "dir -> src created")
    os.mkdir("src\\utils")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> src\\utils created")
    os.mkdir("src\\modules")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> src\\modules created")
    os.mkdir("src\\utils\\helpers")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> src\\utils\\helpers created")
    os.mkdir("src\\utils\\handlers")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> src\\utils\\handlers created")
    os.mkdir("config")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> config created")
    os.mkdir("logs")
    LoggerHandler.log(__name__, LoggingType.INFO, "dir -> logs created")
    with open("src\\utils\\handlers\\LoggerHandler.py", "w") as file:
        file.write(
"""import json
import logging.config
import logging
from src.utils.handlers.LoggingType import LoggingType

class LoggerHandler:
    @staticmethod
    def log(location: str,log_mode: LoggingType, msg: str):
        logging.getLogger(location).log(log_mode.value, msg)

    @staticmethod
    def setup_logging():
        try:
            with open("config\\\\logger.json","r") as file:
                conf_dict = json.loads(file.read())
            logging.config.dictConfig(conf_dict)
            LoggerHandler.log(__name__,LoggingType.DEBUG, "logger set up completed successfully")
        except ValueError as e:
            print("Configuration validation error:", e)
"""
        )
    LoggerHandler.log(__name__, LoggingType.INFO, "file -> src\\utils\\handlers\\LoggingType.py created")
    with open("src\\utils\\handlers\\LoggingType.py", "w") as file:
        file.write(
            """from enum import Enum
import logging
class LoggingType(Enum):
    INFO=logging.INFO
    DEBUG=logging.DEBUG
    WARNING=logging.WARNING
    FATAL=logging.FATAL
    CRITICAL=logging.CRITICAL"""
            )
    LoggerHandler.log(__name__, LoggingType.INFO, "file -> src\\utils\\handlers\\LoggingType.py created")

    with open("config\\logger.json", "w") as file:
        file.write(
"""{
  "version": 1,
  "incremental": false,
  "disable_existing_loggers": true,
  "formatters": {
    "formatter_default": {
      "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
      "datefmt": "%d/%m/%y ( %H:%M:%S )"
    }
  },
  "handlers": {
    "file": {
      "class": "logging.FileHandler",
      "level": "DEBUG",
      "formatter": "formatter_default",
      "filename": "logs\\\\logs.log"
    },
    "console": {
      "class": "logging.StreamHandler",
      "level": "INFO",
      "formatter": "formatter_default",
      "stream": "ext://sys.stdout"
    }
  },
  "loggers": {

  },
  "root": {
    "handlers": [
      "console",
      "file"
    ],
    "level": "DEBUG"
  }
}"""
        )
    LoggerHandler.log(__name__, LoggingType.INFO, "file -> config\\logger.json created")

    with open("main.py","w") as file:
        file.write(
"""from src.utils.handlers.LoggerHandler import LoggerHandler
from src.utils.handlers.LoggingType import LoggingType
            
if __name__ == "__main__":
    LoggerHandler.setup_logging()"""
        )
    LoggerHandler.log(__name__, LoggingType.INFO, "file -> main.py created")

    LoggerHandler.log(__name__, LoggingType.INFO, "all set up!")
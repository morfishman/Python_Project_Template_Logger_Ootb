import json
import logging.config
import logging
from LoggingType import LoggingType

class LoggerHandler:
    @staticmethod
    def log(location: str,log_mode: LoggingType, msg: str):
        logging.getLogger(location).log(log_mode.value, msg)

    @staticmethod
    def setup_logging():
        try:
            conf_dict = json.loads(
"""
{
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
      "console"
    ],
    "level": "DEBUG"
  }
}""")
            logging.config.dictConfig(conf_dict)
            LoggerHandler.log(__name__,LoggingType.DEBUG, "logger set up completed successfully")
        except ValueError as e:
            print("Configuration validation error:", e)

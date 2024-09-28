from enum import Enum
import logging
class LoggingType(Enum):
    INFO=logging.INFO
    DEBUG=logging.DEBUG
    WARNING=logging.WARNING
    FATAL=logging.FATAL
    CRITICAL=logging.CRITICAL
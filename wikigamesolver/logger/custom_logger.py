import logging
import os
import enum

class log_levels(enum.Enum) :
    DEBUG=logging.DEBUG
    INFO=logging.INFO
    WARNING=logging.WARNING
    ERROR=logging.ERROR
    CRITICAL=logging.CRITICAL

def setup_custom_logger(name, level, file, format='[%(asctime)s] %(name)s %(levelname)s - %(message)s', console_logging=False) :
    logger = logging.getLogger(name)
    logger.setLevel(level)

    log_path = os.path.join(os.path.dirname(__file__), file)

    #logging entry format
    logger_formatter = logging.Formatter('[%(asctime)s] %(name)s %(levelname)s - %(message)s')

    logger_handler = logging.FileHandler(log_path)
    logger_handler.setLevel(level)
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)

    if(console_logging):
        console_logger_handler = logging.StreamHandler()
        console_logger_handler.setLevel(level)
        console_logger_handler.setFormatter(logger_formatter)
        logger.addHandler(console_logger_handler)

    return logger
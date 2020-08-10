from .logger import custom_logger

logger = custom_logger.setup_custom_logger(name=__name__,
        level="INFO",
        file="../logs/app.log")

logger.debug("created app.log")

__version__ = '0.1.0'
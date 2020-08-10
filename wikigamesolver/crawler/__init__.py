from wikigamesolver.logger import custom_logger

logger = custom_logger.setup_custom_logger(name=__name__,
        level="DEBUG",
        file="../logs/crawler.log",
        console_logging=True)

logger.debug("created crawler.log")
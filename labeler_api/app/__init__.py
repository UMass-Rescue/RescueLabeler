import logging
from logging.handlers import TimedRotatingFileHandler
import sys
import os
import app.core.config as config


def setup_logging(logger_name, log_file="rescue_labeler.log", log_level="INFO"):
    """Setup logging with rotating file handler

    :param str logger_name: name of logger, 'rescue-labeler'
    :param str log_file: log file name, default
    :param str log_level: Logger output level, default INFO
    :return: logger
    :rtype: logger

    """
    logger = logging.getLogger(logger_name)
    stdout_handler = logging.StreamHandler(sys.stdout)

    log_dir = os.path.join(config.LOG_DIR)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    base_filename = os.path.join(log_dir, log_file)
    file_handler = TimedRotatingFileHandler(base_filename, when="midnight")

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    stdout_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.getLevelName(log_level))

    return logger

# coding=utf-8
import logging
import sys
import os


def setup_logging():
    # get the directory name from the specified path.
    dir_name = os.path.dirname(__file__)
    print(dir_name)

    # create logger and set level
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create console handlers
    c_handler = logging.StreamHandler(sys.stdout)  # đưa log ra màn hình console
    f_handler = logging.FileHandler(dir_name + '/log-data.log')  # ghi log vào file đặt log
    log_format = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

    # set format for loggers and handlers
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # add handlers to logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


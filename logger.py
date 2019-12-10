# coding: utf8
# works on python3.6+


import logging
from sys import stdout


class Clogger:
    logger_name = "C_LOGGER"

    def __init__(self, log_level=logging.INFO, environ=""):
        self.historic = []
        environ = environ
        _logger = logging.getLogger(self.logger_name)
        _logger.setLevel(level=log_level)
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
        stdout_handler = logging.StreamHandler(stream=stdout)
        stdout_handler.setLevel(level=log_level)
        stdout_handler.setFormatter(fmt=formatter)
        file_handler = logging.FileHandler(filename='today.log', mode='a')
        file_handler.setLevel(level=log_level)
        file_handler.setFormatter(fmt=formatter)
        if len(_logger.handlers) < 1:
            _logger.addHandler(hdlr=stdout_handler)
            _logger.addHandler(hdlr=file_handler)

    def get_logger(self):
        return logging.getLogger(name=self.logger_name)

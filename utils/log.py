import logging
import logging.handlers
import sys
from pathlib import Path 
import os

class LoggerConfig:
    @staticmethod
    def set_socket_handler(logger:logging.Logger, host, port):
        handler = logging.handlers.SocketHandler(host, port)
        handler.setFormatter(LoggerConfig._formatter())
        logger.addHandler(handler)

    @staticmethod
    def set_stream_handler(logger:logging.Logger):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(LoggerConfig._formatter())
        logger.addHandler(handler)
    
    @staticmethod
    def set_file_handler(logger:logging.Logger, file_path='logs/app.log'):
        os.makedirs(str(Path(file_path).parent),exist_ok=True)
        handler = logging.FileHandler(file_path)
        handler.setFormatter(LoggerConfig._formatter())
        logger.addHandler(handler)

    @staticmethod
    def _formatter():
        return logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
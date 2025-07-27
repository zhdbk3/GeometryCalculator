import os
import datetime
import logging
import sys

os.makedirs('log', exist_ok=True)

filename = f'log/log_{datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")}.txt'

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s %(levelname)s %(name)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler(), logging.FileHandler(filename, encoding='utf-8')]
)

frontend_logger = logging.getLogger('前端')
backend_logger = logging.getLogger('后端')


def excepthook(exc_type: type[BaseException], exc_value: BaseException, exc_traceback) -> None:
    backend_logger.error(exc_value)


sys.excepthook = excepthook

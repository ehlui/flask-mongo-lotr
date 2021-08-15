from pymongo.errors import ConnectionFailure
from .database import Database
import logging


def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d] ; %(levelname)s ; '
        '[%(name)s.%(funcName)s:%(lineno)d] ; %(message)s',
        datefmt='%d-%m-%Y_%H:%M:%S'
    )


def configure_logging(app, path='logs/app.log'):
    del app.logger.handlers[:]
    loggers = [app.logger, ]
    handlers = []
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    handlers.append(console_handler)

    file_handler = logging.FileHandler(path)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(verbose_formatter())
    handlers.append(file_handler)

    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)


def get_connection(app, db_data):
    try:
        dbi = Database(
            host=db_data['host'], port=db_data['port'],
            db=db_data['db_name'], db_type=db_data['db_type']
        )
        conn = dbi.connection()
    except ConnectionFailure:
        err_msg = "Server not available"
        app.logger.info(err_msg)
        return None
    return conn

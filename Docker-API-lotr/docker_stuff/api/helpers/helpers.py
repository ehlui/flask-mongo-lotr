import logging
import os

db_data = {
    'host': os.getenv("MONGODB_SERVICE_NAME", "No exist"),
    'port': int(os.getenv("MONGODB_PORT", "0000")),
    'db_name': os.getenv("MONGODB_DATABASE", "No exist"),
    'db_type': os.getenv("DATABASE_TYPE", "No exist")
}


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

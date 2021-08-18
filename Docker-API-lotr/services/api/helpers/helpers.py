from flask import current_app as app
import logging
import pymongo
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


def handle_pag_args(limit, offset):
    args_parsed = {'limit': 1, 'offset': 1}
    try:
        limit_parsed = int(limit)
        offset_parsed = int(offset)
        if offset_parsed < 0 or limit_parsed < 0:
            raise ArithmeticError('Offset and limit cannot be smaller than 0')
        args_parsed['limit'] = limit_parsed
        args_parsed['offset'] = offset_parsed
    except (ValueError, ArithmeticError) as e:
        app.logger.error(f' ; msg={e}')
    return args_parsed


def handle_pagination(limit_arg, offset_arg, endpoint):
    pagination = {'prev_url': '', 'next_url': ''}
    arg_dict = handle_pag_args(limit_arg, offset_arg)

    offset_limit_diff = arg_dict["offset"] - arg_dict["limit"]
    prev_args = f'limit={arg_dict["limit"]}&offset={offset_limit_diff}'
    next_args = f'limit={arg_dict["limit"]}&offset={arg_dict["offset"] + arg_dict["limit"]}'

    pagination['prev_url'] = f'{endpoint}?{prev_args}'
    pagination['next_url'] = f'{endpoint}?{next_args}'

    if offset_limit_diff < 0:
        pagination['prev_url'] = ''

    return pagination


def build_pagination(limit_arg, offset_arg, endpoint, element, db_table):
    arg_dict = handle_pag_args(limit_arg, offset_arg)
    pag_urls = handle_pagination(
        arg_dict['limit'], arg_dict['offset'], endpoint
    )

    limit = arg_dict['limit']
    offset = arg_dict['offset']

    start_id = db_table.find().sort(element, pymongo.ASCENDING)
    last_id = start_id[offset][element]

    pagination_search = {element: {'$gte': last_id}}

    return {
        'limit': limit,
        'offset': offset,
        'prev_url': pag_urls["prev_url"],
        'next_url': pag_urls["next_url"],
        'pagination_search': pagination_search
    }

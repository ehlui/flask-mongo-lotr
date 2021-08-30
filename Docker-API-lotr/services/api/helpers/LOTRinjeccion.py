"""
Script for inject all data from api/data to the mongo service
"""
import json
import os
from .helpers import configure_logging
from os.path import dirname, abspath

PARENT_PATH = str(dirname(dirname(abspath(__file__))))
LOG_PATH = os.path.join(PARENT_PATH, 'logs', 'app.log')


def insert_data(file_path, table_name, conn):
    with open(file_path) as file:
        data_read = file.read()
        json_obj_list = json.loads(data_read)
        if conn is not None:
            for json_obj in json_obj_list:
                conn[table_name].insert_one(json_obj)


def get_data(table_name, conn):
    if conn is not None:
        table_elements = conn[table_name].find()
        for element in table_elements:
            print(element)


def drop_data(table_name, conn):
    if conn is not None:
        conn[table_name].drop()


def main(app, db_conn):
    if db_conn is None:
        raise Exception('database instance is none')

    configure_logging(app, path=LOG_PATH)

    data_path = os.path.join(PARENT_PATH, 'data')

    books_path = os.path.join(data_path, 'books.json')
    chapters_path = os.path.join(data_path, 'chapters.json')  # chapters.json
    movies_path = os.path.join(data_path, 'movies.json')
    characters_path = os.path.join(data_path, 'characters.json')

    print('Script for injecting data to the mongo database!')

    dict_lotr_tables_paths = {
        'books': books_path,
        'chapters': chapters_path,
        'characters': characters_path,
        'movies': movies_path,

    }
    response = 'Data injected'
    try:
        for table_name in dict_lotr_tables_paths.keys():
            drop_data(table_name, db_conn)

        for table_name, file_path in dict_lotr_tables_paths.items():
            insert_data(file_path, table_name, db_conn)

        for table_name in dict_lotr_tables_paths.keys():
            get_data(table_name, db_conn)
    except Exception as e:
        response = f'err--{e}'
    return response


if __name__ == '__main__':
    main(db_conn=None)

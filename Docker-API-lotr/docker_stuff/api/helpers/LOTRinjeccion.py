"""
Script for inject all data from api/data to the mongo service
"""
import os
import sys
import json
from pathlib import Path
from flask import Flask
from helpers import configure_logging, get_connection

path = Path(os.getcwd())
API_BASE_PATH = str(path.parents[0])
sys.path.append(API_BASE_PATH)

from custom_settings.settings import db_data_lotr

app = Flask(__name__)
configure_logging(app, path='../logs/app.log')


def insert_data(file_path, table_name):
    with open(file_path) as file:
        data_read = file.read()
        json_obj_list = json.loads(data_read)
        conn = get_connection(app, db_data_lotr)
        if conn is not None:
            for json_obj in json_obj_list:
                conn[table_name].insert_one(json_obj)


def get_data(table_name):
    conn = get_connection(app, db_data_lotr)
    if conn is not None:
        table_elements = conn[table_name].find()
        for element in table_elements:
            print(element)


def drop_data(table_name):
    conn = get_connection(app, db_data_lotr)
    if conn is not None:
        conn[table_name].drop()


def main():
    books_path = '../data/books.json'
    chapters_path = '../data/chapters.json'
    movies_path = '../data/movies.json'
    characters_path = '../data/characters.json'

    print('Script for injecting data to the mongo database!')

    dict_lotr_tables_paths = {
        'books': books_path,
        'chapters': chapters_path,
        'characters': characters_path,
        'movies': movies_path,

    }

    for table_name in dict_lotr_tables_paths.keys():
        drop_data(table_name)

    for table_name, file_path in dict_lotr_tables_paths.items():
        insert_data(file_path, table_name)

    for table_name in dict_lotr_tables_paths.keys():
        get_data(table_name)


if __name__ == '__main__':
    main()

import os
import pytest
import requests
import json
from ..tolkien.database import Database
from ..helpers.helpers import db_data
from ..helpers import get, post, delete


def insert_data(file_path, table_name, conn):
    with open(file_path) as file:
        data_read = file.read()
        json_obj_list = json.loads(data_read)
        if conn is not None:
            for json_obj in json_obj_list:
                conn[table_name].insert_one(json_obj)


def drop_data(table_name, conn):
    if conn is not None:
        conn[table_name].drop()


@pytest.fixture
def context():
    api_name = 'tolkien'
    base_url = f'http://localhost:5000/{api_name}'
    db = Database(db_data).get_database()

    if db is None:
        Database.raise_database_none()

    delete('books', db)
    delete('movies', db)
    delete('chapters', db)

    post('data/books.json', 'books', db)
    post('data/movies.json', 'movies', db)
    post('data/chapters.json', 'chapters', db)

    return {'base_url': base_url}


def test_get_index_request(context):
    response = requests.get(context['base_url'])
    assert response.ok


def test_get_books_request(context):
    books_url = f"{context['base_url']}/books"
    response = requests.get(books_url)
    result = response.json()['books']
    expected_result = [
        {'name': 'The Fellowship Of The Ring'},
        {'name': 'The Two Towers'},
        {'name': 'The Return Of The King'}
    ]
    assert response.ok
    assert expected_result == result


def test_get_movies_request(context):
    books_url = f"{context['base_url']}/movies"
    response = requests.get(books_url)
    result = response.json()['movies']
    expected_result = [{"name": "The Hobbit Series",
                        "runtimeInMinutes": 462,
                        "budgetInMillions": 675,
                        "boxOfficeRevenueInMillions": 2932,
                        "academyAwardNominations": 7,
                        "academyAwardWins": 1,
                        "rottenTomatoesScore": 66.33333333}]
    assert response.ok
    assert expected_result == result


def test_get_chapters_request(context):
    books_url = f"{context['base_url']}/chapters"
    response = requests.get(books_url)
    result = response.json()['chapters']
    expected_result = [{"chapter_name": "A Long-expected Party",
                        "book": "The Fellowship Of The Ring",
                        "chapter": 1}]
    assert response.ok
    assert expected_result == result

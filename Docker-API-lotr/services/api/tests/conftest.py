import os
import pytest
import requests

FILES_FOLDER = "data"
BOOKS_FILE_PATH = os.path.join(FILES_FOLDER, "books.json")
CHAPTERS_FILE_PATH = os.path.join(FILES_FOLDER, "chapters.json")
MOVIES_FILE_PATH = os.path.join(FILES_FOLDER, "movies.json")

BASE_ENDPOINT = '/tolkien'
BASE_URL = 'http://localhost:5000/tolkien/'


def test_get_individual_request():
    response = requests.get(BASE_URL)
    assert response.ok is True

from flask import Blueprint, url_for, redirect, render_template, jsonify
from ..helpers.LOTRinjeccion import main as inject_data
from ..helpers.helpers import db_data
from .database import Database

APP_NAME = 'tolkien'
tolkien = Blueprint(APP_NAME, __name__, template_folder="templates/tolkien")
db = Database(db_data).get_database()


@tolkien.route("/home")
@tolkien.route("/")
def home():
    return render_template('index.html')


@tolkien.route('/inject-data')
def data_injection():
    return inject_data(db)


@tolkien.app_errorhandler(404)
def error_page(e):
    return redirect(url_for(f'{APP_NAME}.page_not_found'))


@tolkien.route("/error-404")
def page_not_found():
    return render_template('404.html'), 404


@tolkien.route('/books')
def get_books():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['books'].find()
        book_list = []
        for element in table_elements:
            book = {'id': element['_id'], 'name': element['name']}
            book_list.append(book)
        response = jsonify({"books": book_list})
    return response


@tolkien.route('/chars')
@tolkien.route('/characters')
def get_characters():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['characters'].find()
        char_list = []
        for element in table_elements:
            char = {
                'id': element['_id'], 'death': element['death'],
                'birth': element['birth'], 'hair': element['hair'],
                'realm': element['realm'], 'height': element['height'],
                'spouse': element['realm'], 'gender': element['height'],
                'name': element['name'], 'race': element['race']
            }
            char_list.append(char)
        response = jsonify({"characters": char_list})
    return response

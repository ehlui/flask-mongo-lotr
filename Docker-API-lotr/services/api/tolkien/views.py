from flask import Blueprint, url_for, redirect, render_template, jsonify, request
from ..helpers.LOTRinjeccion import main as inject_data
from ..helpers.helpers import db_data, build_pagination
from .database import Database
from flask import current_app as app
import pymongo

APP_NAME = 'tolkien'
tolkien = Blueprint(APP_NAME, __name__, template_folder="templates/tolkien")
db = Database(db_data).get_database()


@tolkien.route("/home")
@tolkien.route("/")
def home():
    return render_template('index.html')


@tolkien.route('/inject-data')
def data_injection():
    app.logger.info('endpoint=/inject-data ; msg=Injecting data to the database')
    return inject_data(db)


@tolkien.app_errorhandler(404)
def error_page(e):
    app.logger.info(f'endpoint=/tolkien/? ; msg={e}')
    return redirect(url_for(f'{APP_NAME}.page_not_found'))


@tolkien.route("/error-404")
def page_not_found():
    return render_template('404.html'), 404


@tolkien.route('/movies')
def get_movies():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['movies'].find()
        movies_list = []
        for element in table_elements:
            movies_list.append(element)
        response = jsonify({"movies": movies_list})
    app.logger.info(f'endpoint=/tolkien/movies ; msg={response}')
    return response


@tolkien.route('/chapters')
def get_chapters():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['chapters'].find()
        chapters_list = []
        for element in table_elements:
            chapters_list.append(element)
        response = jsonify({"chapters": chapters_list})
    app.logger.info(f'endpoint=/tolkien/chapters ; msg={response}')
    return response


@tolkien.route('/chap_test')
def get_chaptest():
    response = {'data': 'None'}
    if db is not None:
        chapter = db['chapters']
        endpoint = f'{APP_NAME}/chap_test'
        element = 'chapter'

        limit_arg = request.args.get('limit', 10)
        offset_arg = request.args.get('offset', 0)

        pag_dict = build_pagination(
            limit_arg, offset_arg, endpoint, element, chapter
        )
        chapters = chapter \
            .find(pag_dict["pagination_search"]) \
            .sort(element, pymongo.ASCENDING) \
            .limit(pag_dict["limit"])
        output = []
        for c in chapters:
            output.append(c)

        response = jsonify(
            {
                "result": output,
                'prev_url': pag_dict["prev_url"],
                'next_url': pag_dict["next_url"]
            }
        )
    app.logger.info(f'endpoint=/tolkien/chap_test ; msg=test_pagination')
    return response


@tolkien.route('/books')
def get_books():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['books'].find()
        book_list = []
        for element in table_elements:
            book_list.append(element)
        response = jsonify({"books": book_list})
    app.logger.info(f'endpoint=/tolkien/books ; msg={response}')
    return response


@tolkien.route('/chars')
@tolkien.route('/characters')
def get_characters():
    response = {'data': 'None'}
    if db is not None:
        table_elements = db['characters'].find()
        char_list = []
        for element in table_elements:
            char_list.append(element)
        response = jsonify({"characters": char_list})
    app.logger.info(f'endpoint=/tolkien/chars ; msg=characters_list')
    return response

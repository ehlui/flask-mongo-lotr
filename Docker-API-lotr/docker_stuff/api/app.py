from flask import Flask, jsonify
from flask import request
from .helpers.helpers import configure_logging, get_connection
from .custom_settings.settings import db_data_lotr

app = Flask(__name__)
configure_logging(app)


@app.route('/')
def hello():
    app.logger.info(f'ip={request.remote_addr}; status=200; method={request.method}')
    return jsonify(
        status=True,
        message='Welcome to a Dockerized Flask MongoDB app!'
    )


@app.route('/books')
def get_books():
    conn = get_connection(app, db_data_lotr)
    response = {'data': 'None'}
    if conn is not None:
        table_elements = conn['books'].find()
        book_list = []
        for element in table_elements:
            book = {'id': element['_id'], 'name': element['name']}
            book_list.append(book)
        response = jsonify({"books": book_list})
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

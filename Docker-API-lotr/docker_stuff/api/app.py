from flask import Flask, jsonify
from flask import request
from .helpers.helpers import configure_logging, get_connection

app = Flask(__name__)
configure_logging(app)

DB_TEST_TABLE_NAME = 'animal_tb'

db_animal_data = {
    'host': 'db-mongo',
    'port': 27017,
    'db_name': 'animal_db',
    'db_type': 'mongo'
}


@app.route('/animals')
def get_stored_animals():
    conn = get_connection(app, db_animal_data)
    response = None
    if conn is not None:
        _animals = conn[DB_TEST_TABLE_NAME].find()
        animals_list = []
        for animal in _animals:
            animal_data = {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            animals_list.append(animal_data)
        app.logger.info(f'endpoint=/animals; ip={request.remote_addr}; status=200; method={request.method}')
        response = jsonify({"animals": animals_list})
    return response


@app.route('/')
def hello():
    app.logger.info(f'ip={request.remote_addr}; status=200; method={request.method}')
    return jsonify(
        status=True,
        message='Welcome to the Dockerized Flask MongoDB app!'
    )


@app.route('/js', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # two keys are needed because of the nested object
    python_version = request_data['version_info']['python']

    # an index is needed because of the array
    example = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
               The language value is: {}
               The framework value is: {}
               The Python version is: {}
               The item at index 0 in the example list is: {}
               The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)

from flask import Flask, jsonify
from flask import request
from .helpers.helpers import configure_logging
from .tolkien.views import tolkien as tolkien_app

app = Flask(__name__)
configure_logging(app)
app.register_blueprint(tolkien_app, url_prefix='/tolkien')


@app.route('/')
def hello():
    app.logger.info(
        f'ip={request.remote_addr}; '
        f'status=200; method={request.method}'
    )
    return jsonify(
        {"status": 'OK'}
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

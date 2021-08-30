from flask import request, redirect
from . import create_app, BASE_ENDPOINT

# app = Flask(__name__)
# configure_logging(app)
# BASE_ENDPOINT = '/tolkien'

# app.register_blueprint(tolkien_app, url_prefix=BASE_ENDPOINT)
app = create_app()


@app.route('/')
def hello():
    app.logger.info(
        f'ip={request.remote_addr}; '
        f'status=200; method={request.method}'
    )
    return redirect(location=BASE_ENDPOINT)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

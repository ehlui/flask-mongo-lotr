from .tolkien.views import tolkien as tolkien_app
from .helpers.helpers import configure_logging
from flask import Flask

BASE_ENDPOINT = "/tolkien"


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        ...
    else:
        # load the test config if passed in
        app.config.update(test_config)

    configure_logging(app)

    # apply the blueprints to the app
    # from .tolkien.views import tolkien as tolkien_app

    app.register_blueprint(tolkien_app, url_prefix=BASE_ENDPOINT)

    return app

from flask import Flask
from flask_restful import Api

from repository.sql import dbRel


def create_app():
    app = Flask(__name__)
    dbRel.init_app(app)

    # API
    api = Api(app, catch_all_404s=True)

    # Add resources
    # todo add resources

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

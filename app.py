from flask import Flask
from config import Config
from extensions import api, cors
from routes.riego_routes import ns


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    api.init_app(app)
    api.add_namespace(ns)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )
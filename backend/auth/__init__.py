from flask import Flask
from backend.auth.routes import auth_route


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_route, url_prefix='')
    return app

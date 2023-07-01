from flask import Flask
from backend.auth.routes import auth_route
from frontend import root_dir
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_route, url_prefix='')
    # Define o caminho relativo para o diretório de templates
    template_dir = os.path.join(root_dir, 'templates')
    static_dir = os.path.join(root_dir, 'static')
    
    app.static_folder = static_dir
   

    # Configura o caminho do diretório de templates
    app.jinja_loader.searchpath.append(template_dir)

    return app

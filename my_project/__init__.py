import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
from my_project.auth.route import register_routes
from flasgger import Swagger


load_dotenv() 

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Database
db = SQLAlchemy()

def create_app() -> Flask:
    app = Flask(__name__)

    # Конфіг
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config['SWAGGER'] = {
        'title': 'My Project API',
        'uiversion': 3
    }

    Swagger(app)

    _init_db(app)
    register_routes(app)

    return app

def _init_db(app: Flask) -> None:
    db.init_app(app)

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()

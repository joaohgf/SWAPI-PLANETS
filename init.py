from flask import Flask
from database.db import database
from sqlalchemy import create_engine


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] \
        = create_engine("postgresql://postgres:admin@localhost:5432/database")
    app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.app_context().push()
    database.init_app(app)
    database.create_all()
    return app

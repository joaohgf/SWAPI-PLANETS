from flask import Flask
from database.db import database


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'postgresql:///admin:admin@localhost/b2w'
    app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.app_context().push()
    database.init_app(app)
    database.create_all()
    return app

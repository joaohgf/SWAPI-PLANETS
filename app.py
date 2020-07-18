from flask import Flask
from flask_restful import Api
from resource.planets import Planets, Planet, FindByName


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_db():
    database.create_all()


api.add_resource(Planets, '/api/av1/planets/')
api.add_resource(Planet, '/api/av1/planet/<int:planet_id>/')
api.add_resource(FindByName, '/api/av1/planet/name/<string:name>/')

if __name__ == '__main__':
    from database.db import database

    database.init_app(app)
    app.run(debug=True)

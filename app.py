from flask import jsonify
from BLACKLIST import BLACKLIST
from resource.planets import Planets, Planet, GetPlanetsByName, CreatePlanet
from resource.user import User, CreateUser, Login, Logout
from flask_jwt_extended import JWTManager
from init import create_app
from flask_restful import Api


app = create_app()
api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def access_token_invalid():
    return jsonify({"message": "You're logged out"})


api.add_resource(CreatePlanet, '/api/av1/planet/create/')
api.add_resource(Planet, '/api/av1/planet/<int:planet_id>/')
api.add_resource(GetPlanetsByName, '/api/av1/planet/name/<string:name>/')
api.add_resource(Planets, '/api/av1/planets/')
api.add_resource(CreateUser, '/api/av1/user/create/')
api.add_resource(Login, '/api/av1/user/login/')
api.add_resource(User, '/api/av1/user/<int:user_id>/')
api.add_resource(Logout, '/api/av1/user/logout/')


if __name__ == '__main__':
    app.run(debug=True)

from flask_restful import Resource, reqparse
from controller.user import UserController
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from BLACKLIST import BLACKLIST


args = reqparse.RequestParser()
args.add_argument(
    "login", type=str, required=True, help="Missing login")
args.add_argument(
    "password", type=str, required=True, help="Missing password"
)


class User(Resource):

    @classmethod
    def get(cls, user_id):
        user = UserController.get_user(user_id)
        if user:
            return user.parse_json()
        return f"Not found user with ID {user_id}"

    @jwt_required
    def delete(self, user_id):
        user = UserController.delete(user_id)
        if user:
            return user.parse_json()
        return f"Not found user with ID {user_id}"


class CreateUser(Resource):
    def post(self):
        data = args.parse_args()
        if UserController.get_user_by_login(data["login"]):
            return f"The {data['login']} was created before"
        user = UserController.post(data)
        if user:
            return user.parse_json(), 201
        # TODO arrumar esse error
        return ""


class Login(Resource):
    def post(self):
        data = args.parse_args()
        user = UserController.get_user_by_login(data["login"])
        if user and safe_str_cmp(user.password, data["password"]):
            access_token = create_access_token(identity=user.user_id)
            return {"access_token": access_token}
        return {"message": "Error in logging, confirm your password or login"}


class Logout(Resource):

    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {"message": "Logged out successfully"}

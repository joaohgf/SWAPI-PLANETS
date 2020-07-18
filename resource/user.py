from flask_restful import Resource, reqparse
from facade.user import UserFacade


class User(Resource):
    def get(self, user_id):
        user = UserFacade.get_user(user_id)

    def post(self):
        args = reqparse.RequestParser()
        args.add_argument(
            "login", type=str, required=True, help="Missing login")
        args.add_argument(
            "password", type=str, required=True, help="Missing password"
        )
        data = args.parse_args()
        user = UserFacade.post(data)
        if user:
            return user
        return f"The {user.name}"

    def delete(self):
        pass


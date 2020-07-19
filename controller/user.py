from models.user import UserModel


class UserController:
    @classmethod
    def get_user(cls, user_id):
        user = UserModel.find_user_by_id(user_id)
        if user:
            return user
        return None

    @classmethod
    def post(cls, data):
        user_object = UserModel(**data)
        user = UserModel.save(user_object)
        if user:
            return user
        return None

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_user_by_id(user_id)
        user.delete()
        if user:
            return user
        return None

    @classmethod
    def get_user_by_login(cls, login):
        user = UserModel.find_user_by_login(login)
        if user:
            return user
        return None

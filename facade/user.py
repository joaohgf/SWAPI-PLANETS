from models.user import User


class UserFacade:
    @classmethod
    def get_user(cls, user_id):
        user = User.find_planet_by_id(user_id)
        if user:
            return user
        return None

    def post(self):
        pass

    def delete(self):
        pass

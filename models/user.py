from database.db import database


class User(database.Model):
    __tablename__ = "user"

    user_id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(50))
    password = database.Column(database.String(50))

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def parse_json(self):
        return {
            "user_id": self.user_id,
            "login": self.login
        }

    @classmethod
    def find_user_by_id(cls, user_id):
        if user_id:
            try:
                user = cls.query.filter_by(user_id=user_id).first()
            except Exception as error:
                return f"Error getting by id: {error}"
            if user:
                return user
            return None

    def save(self):
        try:
            database.session.add(self)
            database.session.commit()
        except Exception as error:
            return f"Error saving {error}"

    def delete(self):
        try:
            database.session.delete(self)
            database.session.commit()
        except Exception as error:
            return f"Error deleting{error}"
        return self.name

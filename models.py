from flask_login import UserMixin
from werkzeug.security import check_password_hash

class User(UserMixin):
    def __init__(self, id, email, password_hash):
        self.id = id
        self.email = email
        self.password_hash = password_hash

    def verificar_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(mysql, email):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, email, password_hash FROM usuarios WHERE email = %s", (email,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return User(*data)
        return None

    @staticmethod
    def get_by_id(mysql, user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, email, password_hash FROM usuarios WHERE id = %s", (user_id,))
        data = cursor.fetchone()
        cursor.close()
        if data:
            return User(*data)
        return None

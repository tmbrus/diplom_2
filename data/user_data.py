import random
import string


class UserData:
    """Класс для генерации данных пользователя"""

    @staticmethod
    def generate_user_body():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return {
            "email": f"test_{random_string}@example.com",
            "password": f"password_{random_string}",
            "name": f"User_{random_string}"
        }

    @staticmethod
    def generate_incomplete_body(missing_field):
        """Генерация тела с пропущенным полем"""
        body = UserData.generate_user_body()
        body[missing_field] = ""
        return body

    @staticmethod
    def get_login_body(email, password):
        return {"email": email, "password": password}


class UserResponses:
    """Ожидаемые ответы от API пользователя"""

    USER_ALREADY_EXISTS = {
        "success": False,
        "message": "User already exists"
    }

    REQUIRED_FIELDS_MISSING = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    INCORRECT_CREDENTIALS = {
        "success": False,
        "message": "email or password are incorrect"
    }


import pytest
from api.user_api import UserApi


@pytest.fixture
def create_user():
    """Фикстура для создания пользователя и возврата токена"""
    from data.user_data import UserData
    user_body = UserData.generate_user_body()
    response = UserApi.create_user(user_body)
    token = response.json()["accessToken"]

    yield token, user_body

    # Удаление пользователя после теста
    UserApi.delete_user(token)


@pytest.fixture
def delete_user():
    """Фикстура для удаления пользователя"""
    tokens = []

    def _delete_user(token):
        tokens.append(token)

    yield _delete_user

    for token in tokens:
        UserApi.delete_user(token)


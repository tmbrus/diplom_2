import pytest
import allure
from api.user_api import UserApi
from data.user_data import UserData, UserResponses


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, delete_user, request):
        user_body = UserData.generate_user_body()
        response = UserApi.create_user(user_body)
        token = response.json()["accessToken"]
        request.node.funcargs["delete_user"] = token
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_registered_user(self, create_user):
        token, user_body = create_user
        response = UserApi.create_user(user_body)
        actual_body = response.json()

        assert response.status_code == 403
        assert actual_body == UserResponses.USER_ALREADY_EXISTS

    @allure.title('Создание пользователя с пустым обязательным полем')
    @pytest.mark.parametrize("missing_field", [
        "email",
        "password",
        "name"
    ], ids=[
        "empty_email",
        "empty_password",
        "empty_name"
    ])
    def test_create_user_with_empty_required_field(self, missing_field):
        user_body = UserData.generate_user_body()
        user_body[missing_field] = ""

        response = UserApi.create_user(user_body)
        actual_body = response.json()

        assert response.status_code == 403
        assert not actual_body.get("success", True)
        assert "required" in actual_body.get("message", "").lower()

    @allure.title('Создание пользователя с отсутствующим обязательным полем')
    @pytest.mark.parametrize("missing_field", [
        "email",
        "password",
        "name"
    ], ids=[
        "missing_email",
        "missing_password",
        "missing_name"
    ])
    def test_create_user_with_missing_required_field(self, missing_field):
        user_body = UserData.generate_user_body()
        user_body.pop(missing_field, None)

        response = UserApi.create_user(user_body)
        actual_body = response.json()

        assert response.status_code == 403
        assert not actual_body.get("success", True)
        assert "required" in actual_body.get("message", "").lower()
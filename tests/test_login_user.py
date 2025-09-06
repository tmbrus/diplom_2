import allure
from api.user_api import UserApi
from data.user_data import UserData, UserResponses


class TestLoginUser:

    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user(self, create_user):
        token, user_body = create_user
        login_body = UserData.get_login_body(user_body["email"], user_body["password"])
        response = UserApi.login_user(login_body)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True
        assert "accessToken" in actual_body

    @allure.title('Вход с неверным логином и паролем')
    def test_login_incorrect_credentials(self):
        login_body = UserData.get_login_body("nonexistent@example.com", "wrongpassword")
        response = UserApi.login_user(login_body)
        actual_body = response.json()

        assert response.status_code == 401
        assert actual_body == UserResponses.INCORRECT_CREDENTIALS
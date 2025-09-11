import requests
import allure
from api.urls import Urls


class UserApi:
    """API методы для работы с пользователем"""

    @staticmethod
    @allure.step("Создание пользователя")
    def create_user(body):
        return requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=body)

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(body):
        return requests.post(Urls.BASE_URL + Urls.LOGIN_USER, json=body)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(Urls.BASE_URL + Urls.DELETE_USER,
                               headers={"Authorization": token})
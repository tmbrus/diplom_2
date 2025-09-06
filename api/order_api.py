import requests
import allure
from data.urls import Urls


class OrderApi:
    """API методы для работы с заказами"""

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, token):
        headers = {"Authorization": token} if token else {}
        return requests.post(Urls.BASE_URL + Urls.CREATE_ORDER, json=body, headers=headers)

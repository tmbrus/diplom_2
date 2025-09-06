import allure
from api.order_api import OrderApi
from data.order_data import OrderData, OrderResponses


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self, create_user):
        token, user_body = create_user
        order_body = OrderData.generate_order_body()
        response = OrderApi.create_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        order_body = OrderData.generate_order_body()
        response = OrderApi.create_order(order_body, "")
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients(self, create_user):
        token, user_body = create_user
        order_body = OrderData.generate_order_body()
        response = OrderApi.create_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == 200
        assert actual_body["success"] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user):
        token, user_body = create_user
        order_body = OrderData.generate_empty_order_body()
        response = OrderApi.create_order(order_body, token)
        actual_body = response.json()

        assert response.status_code == 400
        assert actual_body == OrderResponses.NO_INGREDIENTS

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredients(self, create_user):
        token, user_body = create_user
        order_body = OrderData.generate_invalid_ingredients_body()
        response = OrderApi.create_order(order_body, token)

        assert response.status_code == 500
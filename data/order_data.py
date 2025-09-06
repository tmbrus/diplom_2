class OrderData:
    """Класс с данными для заказов"""

    VALID_INGREDIENTS = [
        "61c0c5a71d1f82001bdaaa6d",  # Булка
        "61c0c5a71d1f82001bdaaa6f",  # Начинка
        "61c0c5a71d1f82001bdaaa72"  # Соус
    ]

    @staticmethod
    def generate_order_body():
        return {"ingredients": OrderData.VALID_INGREDIENTS}

    @staticmethod
    def generate_empty_order_body():
        return {"ingredients": []}

    @staticmethod
    def generate_invalid_ingredients_body():
        return {"ingredients": ["invalid_hash_123"]}


class OrderResponses:
    """Ожидаемые ответы от API заказов"""

    NO_INGREDIENTS = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    UNAUTHORIZED = {
        "success": False,
        "message": "You should be authorised"
    }
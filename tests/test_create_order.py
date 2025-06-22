import allure
import requests
from data.ingredients import INGREDIENTS


ORDER_URL = "https://stellarburgers.nomoreparties.site/api/orders"


@allure.feature("Create Order")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, auth_token):
        headers = {"Authorization": auth_token}
        payload = {"ingredients": INGREDIENTS}
        response = requests.post(ORDER_URL, json=payload, headers=headers, timeout=10)
        assert response.status_code in [200, 201], f"Expected 200 or 201, got {response.status_code}"

    @allure.title("Создание заказа без токена")
    def test_create_order_without_auth(self):
        payload = {"ingredients": INGREDIENTS}
        response = requests.post(ORDER_URL, json=payload, timeout=10)
        assert response.status_code == 401, f"Expected 401, got {response.status_code}"
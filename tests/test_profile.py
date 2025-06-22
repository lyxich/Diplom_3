import allure
from pages.profile_page import ProfilePage


@allure.feature("Profile Page")
class TestProfilePage:

    @allure.title("Переход в историю заказов")
    def test_go_to_orders_history(self, setup, auth_token):
        page = ProfilePage(setup)
        page.go_to_profile()
        page.go_to_orders_history()
        assert "history" in page.get_current_url(), "Не удалось перейти в историю заказов"

    @allure.title("Выход из аккаунта")
    def test_logout(self, setup, auth_token):
        page = ProfilePage(setup)
        page.go_to_profile()
        page.logout()
        assert "login" in page.get_current_url(), "Пользователь не вышел из аккаунта"
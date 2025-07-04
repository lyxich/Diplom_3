from pages.base_page import BasePage
from pages.locators.profile_page_locators import *
import allure


class ProfilePage(BasePage):

    @allure.step("Открыть страницу профиля")
    def go_to_profile(self):
        self.open(PROFILE_PAGE_URL)

    @allure.step("Перейти в историю заказов")
    def go_to_orders_history(self):
        self.click_element(ORDERS_HISTORY_LINK)

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.click_element(LOGOUT_BUTTON)
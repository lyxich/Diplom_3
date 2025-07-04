import allure
from pages.base_page import BasePage
from pages.locators.constructor_page_locators import *


class ConstructorPage(BasePage):

    @allure.step("Перейти в конструктор")
    def open_constructor(self):
        self.open(CONSTRUCTOR_PAGE_URL)

    @allure.step("Кликнуть по ингредиенту")
    def click_ingredient(self):
        self.click_element(INGREDIENT)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_element(MODAL_CLOSE_BUTTON)

    @allure.step("Получить значение каунтера ингредиента")
    def get_ingredient_counter_value(self):
        return int(self.find_element(INGREDIENT_COUNTER).text)

    @allure.step("Нажать оформить заказ")
    def make_order(self):
        self.click_element(MAKE_ORDER_BUTTON)

    @allure.step("Модальное окно открыто")
    def is_modal_opened(self):
        return self.find_element(MODAL_WINDOW).is_displayed()
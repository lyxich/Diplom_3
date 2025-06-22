import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/"

    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
    INGREDIENT = (By.XPATH, "//span[text()='Соус фирменный Space']/ancestor::a")

    @allure.step("Открытие главной страницы")
    def open_main(self):
        self.open(self.URL)

    @allure.step("Переход в Конструктор")
    def go_to_constructor(self):
        self.click_element(self.CONSTRUCTOR_LINK)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(self.INGREDIENT)
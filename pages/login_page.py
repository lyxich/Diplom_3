import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/login"

    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Открытие страницы входа")
    def open_login(self):
        self.open(self.URL)

    @allure.step("Ввод email и пароля")
    def login(self, email, password):
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
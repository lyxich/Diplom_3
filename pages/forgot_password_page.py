import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/forgot-password"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    EMAIL_FIELD = (By.NAME, "email")

    @allure.step("Открытие страницы восстановления пароля")
    def open_restore(self):
        self.open(self.URL)

    @allure.step("Ввод email и клик «Восстановить»")
    def restore_password(self, email):
        self.input_text(self.EMAIL_FIELD, email)
        self.click_element(self.RESTORE_BUTTON)
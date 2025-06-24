import allure
from pages.base_page import BasePage
from pages.locators.recovery_page_locators import *


@allure.step("Страница восстановления пароля")
class RecoveryPage(BasePage):

    @allure.step("Перейти на страницу восстановления пароля")
    def open_recovery(self):
        self.open(RECOVERY_PAGE_URL)

    @allure.step("Нажать кнопку «Восстановить»")
    def click_recovery_button(self):
        self.click_element(RECOVERY_BUTTON)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.input_text(EMAIL_FIELD, email)

    @allure.step("Показать поле пароля")
    def show_password_field(self):
        self.click_element(PASSWORD_SHOW_HIDE_BUTTON)

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        return self.find_element(PASSWORD_FIELD_ACTIVE).is_displayed()
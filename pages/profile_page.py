import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    PROFILE_LINK = (By.LINK_TEXT, "Личный Кабинет")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Выход")

    @allure.step("Переход в Личный кабинет")
    def go_to_profile(self):
        self.open("https://stellarburgers.nomoreparties.site/account/profile")

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
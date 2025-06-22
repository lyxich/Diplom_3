import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/feed"
    FIRST_ORDER = (By.CSS_SELECTOR, ".OrderHistory_link__1iNBY")

    @allure.step("Открытие страницы ленты заказов")
    def open_order_feed(self):
        self.open(self.URL)

    @allure.step("Открытие первого заказа")
    def open_first_order(self):
        self.click_element(self.FIRST_ORDER)

    @allure.step("Проверка наличия заказа в разделе «В работе»")
    def check_order_in_progress(self):
        return self.find_element((By.XPATH, "//ul[@class='OrderFeed_list__OLh56']/li[1]")).is_displayed()
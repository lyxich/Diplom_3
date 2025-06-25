import allure
from pages.base_page import BasePage
from pages.locators.order_feed_page_locators import *


@allure.title("Лента заказов")
class OrderFeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.open(ORDER_FEED_URL)

    @allure.step("Открыть первый заказ")
    def open_first_order(self):
        self.click_element(FIRST_ORDER)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_displayed(self):
        return self.find_element(ORDER_MODAL).is_displayed()

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.find_element(TOTAL_ORDERS_TODAY).text)

    @allure.step("Получить количество выполненных заказов за всё время")
    def get_all_time_orders_count(self):
        return int(self.find_element(TOTAL_ORDERS_ALL_TIME).text)

    @allure.step("Проверить наличие заказа в разделе «В работе»")
    def check_order_in_progress(self):
        return bool(self.find_element(IN_PROGRESS_SECTION).text.strip())
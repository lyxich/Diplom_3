from pages.base_page import BasePage
from pages.locators.order_feed_locators import *


class OrderFeedPage(BasePage):
    def open_order_feed(self):
        self.open(ORDER_FEED_URL)

    def open_first_order(self):
        self.click_element(FIRST_ORDER)

    def check_order_in_progress(self):
        return self.find_element(ORDER_IN_PROGRESS_LOCATOR).is_displayed()

    def get_total_orders(self):
        return int(self.find_element(TOTAL_ORDERS_LOCATOR).text)
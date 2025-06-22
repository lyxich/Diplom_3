from pages.base_page import BasePage
from pages.locators.main_page_locators import *


class MainPage(BasePage):
    URL = MAIN_PAGE_URL

    def open_main(self):
        self.open(self.URL)

    def go_to_constructor(self):
        self.click_element(CONSTRUCTOR_LINK)

    def click_ingredient(self):
        self.click_element(INGREDIENT)

    def make_order(self):
        self.click_element(MAKE_ORDER_BUTTON)
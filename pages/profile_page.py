from pages.base_page import BasePage
from pages.locators.profile_page_locators import *


class ProfilePage(BasePage):
    def go_to_profile(self):
        self.open(PROFILE_PAGE_URL)

    def go_to_orders_history(self):
        self.click_element(ORDERS_HISTORY_LINK)

    def logout(self):
        self.click_element(LOGOUT_BUTTON)
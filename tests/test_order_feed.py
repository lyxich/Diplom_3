import allure
from pages.order_feed_page import OrderFeedPage
from data.user_data import VALID_USER


@allure.feature("Order Feed")
class TestOrderFeed:

    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, setup):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        page.open_first_order()
        modal = page.find_element((By.XPATH, "//div[@class='Modal_modal__container']"))
        assert modal.is_displayed(), "Модальное окно с деталями заказа не открылось"

    @allure.title("Заказ отображается в разделе «В работе»")
    def test_order_appears_in_progress(self, setup):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        assert page.check_order_in_progress(), "Заказ не отображается в разделе «В работе»"
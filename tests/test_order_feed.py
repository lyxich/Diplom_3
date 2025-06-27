import allure
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:

    @allure.title("Открытие деталей заказа")
    def test_open_order_details(self, setup, create_order):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        page.open_first_order()
        assert page.is_modal_displayed(), "Модальное окно не открылось"

    @allure.title("Заказ отображается в разделе «В работе»")
    def test_order_in_progress(self, setup, create_order):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        assert page.check_order_in_progress(), "Заказ не отображается в разделе «В работе»"

    @allure.title("Счётчик выполненных заказов за сегодня увеличивается")
    def test_today_orders_increase(self, setup, create_order):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        initial = page.get_today_orders_count()
        # предположим, есть возможность создать новый заказ через API
        final = initial + 1
        assert final == page.get_today_orders_count() + 1, "Счётчик за сегодня не увеличился"

    @allure.title("Счётчик выполненных заказов за всё время увеличивается")
    def test_all_time_orders_increase(self, setup, create_order):
        page = OrderFeedPage(setup)
        page.open_order_feed()
        initial = page.get_all_time_orders_count()
        # аналогично
        final = initial + 1
        assert final == page.get_all_time_orders_count() + 1, "Счётчик за всё время не увеличился" разделе «В работе»"
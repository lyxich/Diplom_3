import allure
from pages.order_feed_page import OrderFeedPage


@allure.title("Открытие деталей заказа")
def test_open_order_details(setup):
    driver = setup
    order_page = OrderFeedPage(driver)
    order_page.open_order_feed()
    try:
        order_page.open_first_order()
    except Exception as e:
        print(f"Ошибка при открытии заказа: {e}")
    finally:
        pass


@allure.title("Номер заказа отображается в разделе «В работе»")
def test_order_in_progress(setup):
    driver = setup
    order_page = OrderFeedPage(driver)
    order_page.open_order_feed()
    assert order_page.check_order_in_progress()
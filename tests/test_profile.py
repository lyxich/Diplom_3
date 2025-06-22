import allure
from pages.profile_page import ProfilePage


@allure.title("Переход в Личный кабинет")
def test_go_to_profile(setup):
    driver = setup
    profile_page = ProfilePage(driver)
    profile_page.go_to_profile()
    assert "account/profile" in driver.current_url


@allure.title("Переход в историю заказов")
def test_go_to_orders_history(setup):
    driver = setup
    profile_page = ProfilePage(driver)
    profile_page.go_to_profile()
    profile_page.go_to_orders_history()
    assert "account/orders" in driver.current_url


@allure.title("Выход из аккаунта")
def test_logout(setup):
    driver = setup
    profile_page = ProfilePage(driver)
    profile_page.go_to_profile()
    profile_page.logout()
    assert "login" in driver.current_url
import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


@allure.title("Переход на страницу восстановления пароля")
def test_go_to_restore(setup):
    driver = setup
    restore_page = ForgotPasswordPage(driver)
    restore_page.open_restore()
    assert "forgot-password" in driver.current_url


@allure.title("Ввод почты и клик по кнопке «Восстановить»")
def test_fill_email_and_restore(setup):
    driver = setup
    restore_page = ForgotPasswordPage(driver)
    restore_page.open_restore()
    restore_page.restore_password("testuser@example.com")
    assert "reset-password" in driver.current_url


@allure.title("Поле пароля становится активным при клике показать/скрыть")
def test_show_password(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.show_password_field()
    assert login_page.is_password_input_active()
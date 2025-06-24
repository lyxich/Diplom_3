import allure
from pages.recovery_page import RecoveryPage


@allure.feature("Восстановление пароля")
class TestRecoveryPassword:

    @allure.title("Переход к восстановлению пароля")
    def test_go_to_recovery(self, setup):
        page = RecoveryPage(setup)
        page.open_recovery()

    @allure.title("Ввод почты и нажатие «Восстановить»")
    def test_enter_email_and_click_recovery(self, setup):
        page = RecoveryPage(setup)
        page.open_recovery()
        page.enter_email("test@example.com")
        page.click_recovery_button()

    @allure.title("Кнопка показать/скрыть пароль делает поле активным")
    def test_show_password_field_activates_input(self, setup):
        page = RecoveryPage(setup)
        page.open_recovery()
        page.show_password_field()
        assert page.is_password_field_active(), "Поле пароля не стало активным"
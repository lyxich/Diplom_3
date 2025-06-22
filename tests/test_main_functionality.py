import allure
from pages.main_page import MainPage


@allure.feature("Main Page")
class TestMainFunctionality:

    @allure.title("Переход в Конструктор")
    def test_go_to_constructor(self, setup):
        page = MainPage(setup)
        page.open_main()
        page.go_to_constructor()
        assert "constructor" in page.get_current_url(), "URL не содержит 'constructor'"

    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_click_ingredient_opens_modal(self, setup):
        page = MainPage(setup)
        page.open_main()
        page.click_ingredient()
        modal = page.find_element((By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]"))
        assert modal.is_displayed(), "Модальное окно не открылось"
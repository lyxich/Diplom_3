import allure
from pages.constructor_page import ConstructorPage


class TestConstructorFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_open_constructor(self, setup):
        page = ConstructorPage(setup)
        page.open_constructor()

    @allure.title("Открытие деталей ингредиента")
    def test_click_ingredient_opens_modal(self, setup):
        page = ConstructorPage(setup)
        page.open_constructor()
        page.click_ingredient()
        assert page.is_modal_opened(), "Модальное окно не открылось"

    @allure.title("Модальное окно закрывается")
    def test_modal_closes(self, setup):
        page = ConstructorPage(setup)
        page.open_constructor()
        page.click_ingredient()
        page.close_modal()
        assert not page.is_modal_opened(), "Модальное окно не закрылось"

    @allure.title("Каунтер увеличивается при добавлении ингредиента")
    def test_counter_increases_on_add(self, setup):
        page = ConstructorPage(setup)
        page.open_constructor()
        initial = page.get_ingredient_counter_value()
        page.click_ingredient()
        final = page.get_ingredient_counter_value()
        assert final > initial, "Каунтер не увеличился"

    @allure.title("Оформление заказа")
    def test_make_order(self, setup):
        page = ConstructorPage(setup)
        page.open_constructor()
        page.click_ingredient()
        page.make_order()
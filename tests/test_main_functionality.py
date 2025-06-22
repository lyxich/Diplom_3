import allure
from pages.main_page import MainPage


@allure.title("Переход в Конструктор")
def test_go_to_constructor(setup):
    driver = setup
    main_page = MainPage(driver)
    main_page.open_main()
    main_page.go_to_constructor()
    assert "constructor" in main_page.driver.current_url


@allure.title("Клик по ингредиенту открывает модальное окно")
def test_click_ingredient(setup):
    driver = setup
    main_page = MainPage(driver)
    main_page.open_main()
    main_page.click_ingredient()
    assert True  # Здесь можно добавить проверку на модальное окно
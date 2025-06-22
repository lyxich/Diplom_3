from selenium.webdriver.common.by import By

MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"

CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")
MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
INGREDIENT = (By.XPATH, "//span[text()='Соус фирменный Space']/ancestor::a")
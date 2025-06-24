from selenium.webdriver.common.by import By

MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
INGREDIENT = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]/parent::div")
MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter')]")
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
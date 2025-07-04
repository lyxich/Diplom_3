from selenium.webdriver.common.by import By

RECOVERY_PAGE_URL = "https://stellarburgers.nomoreparties.ru/forgot-password"
LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
EMAIL_FIELD = (By.XPATH, "//input[@type='text']")
RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
PASSWORD_SHOW_HIDE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon_action_show')]")
PASSWORD_FIELD_ACTIVE = (By.XPATH, "//input[@type='password' and @class='text input__textfield text_type_main-default']")
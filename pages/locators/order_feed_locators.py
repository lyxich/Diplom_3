from selenium.webdriver.common.by import By

ORDER_FEED_URL = "https://stellarburgers.nomoreparties.ru/feed"
FIRST_ORDER = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')][1]")
ORDER_MODAL = (By.XPATH, "//div[@class='Modal_modal__container']")
TOTAL_ORDERS_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
TOTAL_ORDERS_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_inWork')]")
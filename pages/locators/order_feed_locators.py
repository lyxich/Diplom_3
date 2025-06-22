from selenium.webdriver.common.by import By

ORDER_FEED_URL = "https://stellarburgers.nomoreparties.site/feed"
FIRST_ORDER = (By.CSS_SELECTOR, ".OrderHistory_link__1iNBY")
TOTAL_ORDERS_LOCATOR = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p[1]")
ORDER_IN_PROGRESS_LOCATOR = (By.XPATH, "//ul[@class='OrderFeed_list__OLh56']/li[1]")
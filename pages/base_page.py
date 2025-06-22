from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)
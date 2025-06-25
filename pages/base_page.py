from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.title("Базовая страница")
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент по локатору")
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввести текст '{text}' в поле")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def setup(request):
    browser = request.param
    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()
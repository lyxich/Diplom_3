import pytest
from utils.driver_factory import DriverFactory
from utils.api_helpers import register_user, login_user, delete_user


@pytest.fixture(scope="function")
def auth_token():
    email = "testuser_new@example.com"
    password = "password"
    name = "New User"

    # Регистрация пользователя
    register_response = register_user(email, password, name)

    if register_response.status_code not in [200, 201]:
        raise RuntimeError(f"Failed to register user: {register_response.text}")

    # Логин и получение токена
    login_response = login_user(email, password)
    if login_response.status_code != 200:
        raise RuntimeError(f"Failed to login user: {login_response.text}")

    token = login_response.json()['accessToken']

    yield token

    # Удаление после теста
    delete_user(token)


@pytest.fixture(scope="function")
def create_order(auth_token):
    api = ApiClient()
    response = api.create_order(auth_token, ORDER_DATA["simple_burger"])

    if response.status_code != 200:
        pytest.fail(f"Order creation failed with status code {response.status_code}")

    order_data = response.json()

    return order_data  # передаём данные заказа в тесты


@pytest.fixture(scope="function")
def setup(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()
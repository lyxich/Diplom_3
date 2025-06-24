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
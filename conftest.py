import pytest
from utils.driver_factory import DriverFactory
from utils.api_helpers import register_user, login_user, delete_user


@pytest.fixture(scope="function")
def auth_token():
    email = "testuser_new@example.com"
    password = "password"
    name = "New User"

    # Регистрация
    register_response = register_user(email, password, name)
    if register_response.status_code == 403:
        # Если пользователь уже существует — удаляем его и регистрируем заново
        delete_user(login_user(email, password).json()['accessToken'])

        register_response = register_user(email, password, name)

    assert register_response.status_code in [200, 201], f"Unexpected status code: {register_response.status_code}"
    token = login_user(email, password).json()['accessToken']

    yield token

    # Удаление после теста
    delete_user(token)
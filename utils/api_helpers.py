import requests

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

def register_user(email, password, name):
    url = f"{BASE_URL}/auth/register"
    payload = {"email": email, "password": password, "name": name}
    return requests.post(url, json=payload, timeout=10)


def login_user(email, password):
    url = f"{BASE_URL}/auth/login"
    payload = {"email": email, "password": password}
    return requests.post(url, json=payload, timeout=10)


def delete_user(token):
    url = f"{BASE_URL}/auth/user"
    headers = {"Authorization": token}
    return requests.delete(url, headers=headers, timeout=10)
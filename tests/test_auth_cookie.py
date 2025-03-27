import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    json_data = {
  "email": "user@example.com",
  "password": "string",
  "is_active": True,
  "is_superuser": False,
  "is_verified": False
}
    response = await client.post("/auth/register", json=json_data)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_protected_route(client: AsyncClient):
    response = await client.get("/protected-route")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_jwt_login(client: AsyncClient):
    # Данные для авторизации
    login_data = {
        "grant_type": "password",  # Обязательный параметр, должен быть "password"
        "username": "user@example.com",  # Обязательный параметр
        "password": "string",  # Обязательный параметр
        "scope": "",  # Необязательный параметр, отправляем пустым
        "client_id": "string",  # Необязательный параметр, отправляем пустым
        "client_secret": "string",  # Необязательный параметр, отправляем пустым
    }

    # Отправляем POST-запрос на эндпоинт /auth/jwt/login
    response = await client.post(
        "/auth/jwt/login",
        data=login_data,  # Используем `data` для передачи данных в формате x-www-form-urlencoded
    )
    # Проверяем статус код ответа
    assert response.status_code == 204  # Ожидаем статус код 204, если авторизация успешна

    # Проверяем, что в ответе есть cookie
    cookies = response.cookies
    # Проверяем наличие конкретной cookie
    if "fastapiusersauth" not in cookies:
        print("Cookie 'fastapiusersauth' not found in response.")
    else:
        print(f"fastapiusersauth: {cookies['fastapiusersauth']}")

    # Шаг 2: Получение данных профиля с использованием cookie
    headers = {"Cookie": f"fastapiusersauth={cookies['fastapiusersauth']}"}  # Добавление куки в заголовок
    response = await client.get("/users/me", headers=headers)

    # Отладочная информация
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Body: {response.text}")

    assert response.status_code == 200
    assert response.json()["email"] == "user@example.com"

# Flask Приложение

Это веб-приложение на Flask для управления регистрацией пользователей, входом в систему и аутентификацией, а также базовой функциональностью аналитики.

## Возможности

- Регистрация пользователей: Пользователи могут создавать новые учетные записи с помощью имени пользователя и пароля.
- Вход пользователей: Зарегистрированные пользователи могут войти в систему, используя свое имя пользователя и пароль.
- Аутентификация пользователей: Защищенные маршруты могут быть доступны только аутентифицированным пользователям.
- Выход пользователей: Аутентифицированные пользователи могут выйти из своих учетных записей.
- Базовая аналитика: Приложение предоставляет базовую функциональность аналитики, включая анализ линейной регрессии.

## Установка

1. Склонируйте репозиторий:



2. Перейдите в директорию проекта:
``
cd flask-app
``
3. Создайте виртуальное окружение (по желанию):
``
python3 -m venv venv
``
4. Активируйте виртуальное окружение (по желанию):

# Для Linux/macOS
``source venv/bin/activate``

# Для Windows
``venv\Scripts\activate``
5. Установите необходимые зависимости:

``pip install -r requirements.txt``

6. Запустите приложение:
``pyhton app.py``
7. Откройте веб-браузер и перейдите по адресу http://localhost:5000, чтобы получить доступ к приложению.
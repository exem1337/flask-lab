# Flask-приложение с линейной регрессией

Это простое Flask-приложение, которое демонстрирует использование линейной регрессии на странице аналитики.

## Установка

1. Установите Python, если у вас его еще нет. Скачать Python можно с [официального сайта](https://www.python.org/downloads/).

2. Создайте и активируйте виртуальное окружение для вашего проекта:
    ```
    python -m venv venv
    ```
    ```
    # На Windows
    venv\Scripts\activate
    ```
    ```
    # На macOS и Linux
    source venv/bin/activate
    ```

3. Установите необходимые пакеты, выполнив следующую команду в командной строке:
    ```
    pip install -r requirements.txt
    ```

## Запуск

1. После установки всех необходимых пакетов, выполните следующую команду для запуска Flask-приложения:
    ```
    python app.py
    ```

2. Откройте веб-браузер и перейдите по адресу `http://127.0.0.1:5000/` чтобы увидеть ваше Flask-приложение.

## Использование

Приложение имеет несколько страниц:

- **Home (`/home`)**: Главная страница с общей информацией.
- **Analytics (`/analytics`)**: Страница аналитики с примером использования линейной регрессии.
- **About (`/about`)**: Страница с информацией о приложении и авторе.
- **Login (`/login`)**: Страница для входа пользователей.
- **Registration (`/registration`)**: Страница для регистрации новых пользователей.

## Дополнительная информация

- Для запуска приложения на сервере не забудьте изменить параметр `debug` на `False` в файле `app.py`.
- Для изменения стилей, отредактируйте файл `static/css/styles.css`.
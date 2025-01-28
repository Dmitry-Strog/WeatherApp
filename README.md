# Проект “Погода”

## Описание
Веб-приложение для просмотра текущей погоды. Пользователь может зарегистрироваться и добавить в коллекцию одну или несколько локаций (городов, сёл, других пунктов), после чего главная страница приложения начинает отображать список локаций с их текущей погодой.
#### [Техническое задание проекта](https://zhukovsd.github.io/python-backend-learning-course/projects/weather-viewer/)

## Установка и запуск проекта

### 1. Клонирование репозитория
Склонируйте репозиторий:
```bash
git clone https://github.com/Dmitry-Strog/WeatherApp.git
```

### 2. Установите Docker
- [Инструкция по установке Docker](https://docs.docker.com/desktop/)

### 3. Настройка окружения
Создайте файл `.env` :
```bash
POSTGRES_DB=mydatabase
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
HOST=db
PORT=5432

WEATHER_API_KEY= Ключ из личного кабинета OpenWeatherApi

SECRET_KEY= Ключ Django
DEBUG=False
```

### 4. Сборка проекта
```bash
 docker compose -f docker-compose.dev.yml up --build -d
```

## Функционал приложения
### 1. Работа с пользователями:

- Регистрация
- Авторизация
- Logout
- Работа с локациями:

### 2. Поиск:
- Добавление в список
- Просмотр списка локаций, для каждой локации отображается название и температура
- Удаление из списка

## Интерфейс
### Авторизация

Адрес - /user/login/ Страница авторизации пользователя.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/a836ef21-fb62-471b-ad43-dce9cec0e34e">

### Регистрация

Адрес - /user/register/ Страница регистрации пользователя.

<img width="400" alt="image" src="https://github.com/user-attachments/assets/01fb5ec6-7c27-4323-b3ad-1eafcb6da1a9">


Главная страница

Адрес - /

<img width="700" alt="image" src="https://github.com/user-attachments/assets/878b6f22-98bc-45b1-8e2e-d88452f4be8e">

Страница результатов поиска

Адрес - /result_search/ Отображает список добавленных локаций.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/bbb93fb6-3ec9-4570-a58f-e2239e3a81bb">

##  Стек

- Python 3.12
- Poetry
- Django 5.1.3
- PostgreSQL
- docker
- unittest
- requests
- gunicorn
- Nginx
- HTML/CSS(Bootstrap5)



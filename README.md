# Веб-сервис на FastAPI

Этот проект представляет собой простой веб-сервис на FastAPI, который выводит приветственное сообщение. Сообщение можно настроить с помощью параметров запроса.

## Возможности

Выводит приветственное сообщение. Настраиваемые `name` и `message` через параметры запроса GET.

## О работе
Веб-сервис использует FastAPI для обработки HTTP-запросов и Uvicorn в качестве ASGI-сервера. Запросы GET обрабатываются с помощью зависимостей и моделей Pydantic для валидации и парсинга параметров запроса.

#### Pydantic модели
Модель `QueryParams` используется для валидации и парсинга параметров запроса `name` и `message`. Параметры имеют ограничения по длине (от 1 до 200 символов) и значения по умолчанию.
```py
class QueryParams(BaseModel):
    name: constr(min_length=1, max_length=200) = "World"
    message: constr(min_length=1, max_length=200) = "Let's be friends"
```

## Docker

Соберите Docker-образ:
```sh
docker build -t fastapi-web-service .
```

Запустите Docker-контейнер:
```sh
docker run -d -p 8000:8000 fastapi-web-service
```
Доступ к сервису через веб-браузер или curl:
```sh
http://<your_docker_host>:8000/?name=Recruto&message=Давай дружить
```

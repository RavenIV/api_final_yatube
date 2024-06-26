# API проекта Yatube

API обрабатывает запросы на чтение, создание, изменение и удаление публикаций и комментариев сайта для блогов.
С помощью API возможно получить список сообществ, подписаться на другого пользователя, а также просматривать свои подписки.
Для аутентификации пользователей применяются JWT-токены.


### Стек технологий

- Python 3.9
- Django 3.2.16
- Django REST Framework 3.12.4
- Simple JWT 5.3.1
- Djoser 2.2.2


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Документация к API, содержащая примеры запросов и ожидаемых ответов, будет доступна по адресу http://127.0.0.1:8000/redoc/

### Разработчики

Ирина Воронцова ([GitHub](https://github.com/RavenIV))



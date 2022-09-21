Проект демонстрирует частоиспользуемый функционал апи приложений на django rest framework предоставляющих данные через http протокол.

Для установки: 
1. склонировать проект (git clone git@github.com:frqhero/api_final_yatube.git)
2. в корне создать venv (python -m venv venv)
3. активировать venv (source venv/Scripts/activate)
4. установить зависимости (pip install -r requirements.txt)
5. перейти в папку с manage.py (yatube_api)
6. выполнить миграции (python manage.py makemigrations; python manage.py migrate)
7. запустить dev-сервер (python manage.py runserver)

В проекте используются:
-django
-django rest framework
-djoser
...etc.

Собрал и проверил frqhero.

http://127.0.0.1:8000/api/v1/follow/?search=user2 пример запроса для получения подписок с передачей отбора.

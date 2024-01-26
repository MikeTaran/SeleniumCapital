# ReTests_table_fill

Метод, предназначенный для автоматического заполнения 
[Google таблицы](https://docs.google.com/spreadsheets/d/1jG0hdjrUdjMFBYHXyBKRGbBwV0ICxfBPaBkgB98Nuuk/edit?pli=1#gid=540090404),
в которую собираются тесты со статусом `Failed` и имеющие именованный тип бага, например `Bug # 05. Opened a 'Sign up' form instead of a 'Login'`

Основные моменты:

    1. Добавлена проверка аргументов командной строки в `conftest.py`
    2. Добавлены маркеры тестов в `pytest.ini`
    3. Что необходимо:
       - промаркировать тесты: `@pytest.mark.test_01`
       - передать переменную `bid` в тестовый элемент
	
Для работы с Google sheets:

    - Install the Google client library for Python:
    `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
    - если будет запуск с ошибкой доступа к GoogleSheets, удалить токен и попробовать запустить заново
    - если снова будет ошибка, то необходима регистрация в Google Cloud API и создание файла credentials.json:
   https://developers.google.com/sheets/api/quickstart/python
	



Гайды:

* https://www.youtube.com/watch?v=caiR7WAGMVM
* https://www.youtube.com/watch?v=sAgWCbGMzTo&list=PL3JVwFmb_BnSee8RFaRPZ3nykuMRlaQp1&index=1
* https://habr.com/ru/articles/305378/


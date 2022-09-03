### Выполнено в рамках тестового задания для компании Taxideli.ru

1. Клонируйте репозиторий

2. Создайте в корне проекта .env файл (по примеру env-example.txt)

3. Запустите docker-compose
```
docker-compose up -d --build
```
4. Примените миграции
```
docker-compose exec web python manage.py migrate  
```
5. Создайте пользователя
```
docker-compose exec web python manage.py createsuperuser 
```
6. Приложение будет доступно по адресу http://127.0.0.1/

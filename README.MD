# Habra scrap is the best of the world program.
___
# ДЛЯ ДАЛЬНЕЙШЕЙ РАБОТЫ ВАМ ПОНАДОБИТСЯ УСТАНОВЛЕННЫЙ DOCKER И DOCKER-COMPOSE!!!
___
### Для того что-бы убедиться что данный проект работает
### необходимо проделать следующее...

Клонируем проект (для простоты можно склонировать в домашнюю дерикторию)
```
git clone https://github.com/Tim-Ilin/habra_scrap.git
```
Переходим в папку с проектом
```
cd habra_scrap/
docker-compose build
docker-compose up
```
В консоли должно появиться примерно следующее
```
System check identified no issues (0 silenced).
app_1  | July 30, 2020 - 17:37:57
app_1  | Django version 3.0.8, using settings 'habra_scrap.settings'
app_1  | Starting development server at http://0.0.0.0:8000/
```
Для проверки отдаваемого json самое простое открыть в браузере адрес
```
http://127.0.0.1:8000/api/v1/
```
По этому адресу мы получим все существующие записи с пагинацией - ограниченой (10 страницами)

Для проверки получения единичной записи
```
http://127.0.0.1:8000/api/v1/<id>
```
где \<id> это id необходимой записи

### Прогон юнит тестов
Тесты будут работать только после того как вы сделаете
```
docker-compose up
```
потому что только после этого создадутся необходимые таблицы

Итак один из вариантов выполнить тест
```shell script
docker-compose run app sh -c "python manage.py test"
```
# # Клиент - это программа, которая делает запросы на сервер
# # Сервер - это ПО которое ожидает запросы, обрабатыавет эти запросы и отправляет клиенту
# # ответ в виде текста или json или html или xml (ResponseBody)
#
# REST API - это механизм взаимодействия клиента и сервера по протоколу HTTP(s)
# Взаимодействие возможно только при активном клиенте и сервере
#
# Протокол HTTP поддерживает методы
# 1)  GET - это метод, который используется для полученя и отправки небольшого набора
# данных. Отправить можно до 1кб. Тело запроса не поддерживается. Существует
# возможность передать на сервер методом GET параметры. Пример запроса:
# http://site/index.py?login=admin&age=25
# В данном URL используется 2 GET параметра - login и age
#
# 2) POST - метод используется для создания нового элемента на сервере
#     (поддерживает RequestBody, то есть тело запроса в виде json(xml))
# Пример - регистрация нового юзера, готовим тело запроса в виде
# {
#     'login':'admin',
#     'pass':'123'
# }
#
# 3) PUT - используется для обновления данных. Метод также поддерживает
# тело запроса. Кроме тела запроса в URL сервера обычно находится параметр по которому
# находим элемент, который нужно обновить
#
# 4) DELETE - удаление данных. Для удаления достаточно указать только ID элемента,
# который удаляем, но метод допускает и тело запроса
#
# 5) PATCH - частичное обновление объекта
#
# # Для создания REST запроса используйте модуль requests
# Перед запросом к серверу нужно прочитать описание сервера, то есть контракт между
# клиентом и сервером. В этом контракте сказано какие данные принимает сервер, то есть
# полное описание тела запроса.
import json

import requests
# response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
# print(response.text)

# response = requests.get('https://reqres.in/api/users')
# print(response.text)
# Получаем информацию о email первого юзера
# my_dict = json.loads(response.text)
# print(my_dict['data'][0]['email'])

# Метод POST
# Подготовим данные(тело запроса) для отправки в сервис методом POST
# user = '{"name":"Иван","job":"admin"}'
# response = requests.post('https://reqres.in/api/users',user)
# print(response.status_code)
# Коды ответов 200, 201, 205 - означают, что запрос успешно принят и обработан
# print(response.text)
# Если код ответа 500 и выше - это ошибка на стороне сервера. Если данные не были распознаны,
#  то есть тело запроса отличается от допустимого на данном сервере.
# 404 - ресурс, к которому обращаемся - не найден

# Метод DELETE
response = requests.delete('https://reqres.in/api/users/2')
print(response.status_code)
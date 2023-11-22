from socket import *
import time

my_socket = socket(AF_INET,SOCK_STREAM) #создали объект сокет, работающий по протоколу TCP
my_socket.bind(("",8007)) #настроили сокет таким образом, чтобы он принимал запросы на локальный IP
# 127.0.0.1 и порт 8888
my_socket.listen(5) #переходим в режим ожидания запросов и допускаем не более 5 запросов одновременно

while True:
    client,addr = my_socket.accept() #Метод accept возвращает кортеж с информацией о клиенте и об адресе запроса
    data_from_client = client.recv(10000000) #для возможности получить данные от клиента
    answer = f"Вы сообщили: {data_from_client.decode('cp1251')}" #информация для клиента в момент коннекта
    client.send(answer.encode("cp1251")) #преобразовали строковый ответ в байты и отправляем ответ клиенту
    client.close() #завершаем работу с клиентом

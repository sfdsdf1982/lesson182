from socket import *
import time

my_socket = socket(AF_INET,SOCK_STREAM) #создали объект сокет, работающий по протоколу TCP
my_socket.bind(("",8008)) #настроили сокет так, чтобы он принимал запросы по локальному
my_socket.listen(5) #Переходим в режим ожидания запросов и допускаем не более 5 запросов
# одновременно

while True:
    client,addr = my_socket.accept() #принимаем запрос на соединение
    data = client.recv(100000) #получили данные от клиента
    str = data.decode('UTF-8')
    nums = str.split("+")
    result = int(nums[0]) + int(nums[1])
    answer = f"Сумма = {result}"
    client.send(answer.encode('UTF-8'))
    print('Сервер решил задачу и отправил ответ клиенту')
    client.close() #завершаем работу с клиентом

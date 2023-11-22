from socket import *

# AF_INET - указываем, что сокет сетевой
# SOCK_STREAM - указываем, что сокет потоковый

my_socket = socket(AF_INET,SOCK_STREAM)
my_socket.connect(('localhost',8007)) #выполняется запрос к серверу
data_for_server = "Привет, сервер!"
my_socket.send(data_for_server.encode('cp1251'))
answer = my_socket.recv(10000000) #ждем ответ сервера
print('Сообщение от сервера:',answer.decode('cp1251'))
my_socket.close()
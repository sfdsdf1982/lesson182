from socket import *

# AF_INET - указываем, что сокет сетевой
# SOCK_STREAM - указываем, что сокет потоковый

my_socket = socket(AF_INET,SOCK_STREAM)
my_socket.connect(('localhost',8888)) #выполняется запрос к серверу
data_from_server = my_socket.recv(1024 * 1000) #принимаем от сервера не более 1кб информации
my_socket.close()
print(f"Сервер сообщил: {data_from_server.decode('cp1251')}")
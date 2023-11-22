from socket import *

my_socket = socket(AF_INET,SOCK_STREAM)
my_socket.connect(('localhost',8008))
msg = '2+6'
my_socket.send(msg.encode('UTF-8')) #отправили серверу набор байт с информацией
answer = my_socket.recv(100000)
print('Сообщение от сервера: ',answer.decode('UTF-8'))
my_socket.close()
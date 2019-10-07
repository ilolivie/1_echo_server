import socket
from time import sleep

sock = socket.socket()

port= int(input("Введите номер порта: "))
if 0 <= port <= 65535:
    pass
else:
    port = 9090
    
try:
    host = input("Введите имя хоста: ")
    if host == 'localhost':
        pass
    else:
        if 0 <= int(host) <= 255:
            pass
        else:
            host = 'localhost'
except ValueError:
    host = 'localhost'
    print('Введено некорректное имя хоста. По умолчанию - localhost')
    
    
sock.connect((host, port))

print("Введите сообщение.Если хотите завершить работу с сервером, введите exit.")
msg = ""
while True:
    if msg != 'exit':
        msg = input()
        sock.send(msg.encode())
        data = sock.recv(1024)
    else:
        break

sock.close()

print("Работа завершена.")

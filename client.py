import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

print("Введите сообщение.Если хотите завершить работу с сервером, введите exit.")
msg = ""
while True:
    if msg != 'exit':
        msg = input()
        sock.send(msg.encode())
        #data = sock.recv(1024)
    else:
        break

sock.close()

#print("Работа завершена.")

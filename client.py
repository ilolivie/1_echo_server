import socket
from threading import Thread

def listen(sock):
    global msg1
    try:
        while True:
            msg1 = sock.recv(1024)
            msg1 = msg1.decode()
            print(msg1)
    except ConnectionAbortedError:
        pass
        
       
sock = socket.socket()


try:
    port= input("Введите номер порта: ")
    if port == '':
        port = 9090
    port = int(port)
    if type(port) == int and 0 <= port <= 65535:
        pass
    else:
        port = 9090
except ValueError:
    port = 9090
    print("Введен некорректный порт. По умолчанию - 9090.")
    
    

try:
    host = input("Введите имя хоста: ")
    if host == '':
        host = 'localhost'
    elif host == 'localhost':
        pass
    else:
        host_lst = host.split('.')           
        for i in host_lst:
            if 0 <= int(i) <= 255:
                pass
            else:
                host = 'localhost'
except ValueError:
    host = 'localhost'
    print('Введено некорректное имя хоста. По умолчанию - localhost')
    
    
sock.connect((host, port))

print("Введите сообщение.Если хотите завершить работу с сервером, введите exit.")

msg = ""
msg1 = ""
t = Thread(target = listen, args = (sock,))
t.start()
if "Введите имя: " in msg1:
    name = input()
    sock.send(name.encode())
    
while True:
    if msg != 'exit':
        msg = input()
        sock.send(msg.encode())
    else:
        break


    



sock.close()

print("Работа завершена.")

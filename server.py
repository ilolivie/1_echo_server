import socket
import logging as log
import json
from threading import Thread
from datetime import datetime

def workwithusers(conn,addr):
    global lst
    iden = identify(addr[0])
    if iden:
        msg = f'Здравствуйте, {iden}!'
        conn.send(msg.encode())
    else:
        msg = "Введите имя: "
        conn.send(msg.encode())
        name = conn.recv(1024)
        name = name.decode()
        with open ('users.json', "r") as f:
            users = json.load(f)
            users[addr[0]] = name
            with open ('users.json', "w") as f:
                json.dump(users,f)
                msg = f'Здравствуйте, {name}!'
                conn.send(msg.encode())
        conn.send('Новый пользователь записан'.encode())
        

   
    
    IsRunning = True 
    print(f'Пользователь {iden} подсоединился.')
    while IsRunning:
        
        data = conn.recv(1024)
        msg = data.decode() 
        for i in lst:
            if i == conn:
                pass
            else:
                if msg == 'exit':
                    i.send(f'Пользователь {iden} отсоединился.'.encode())
                else:
                    i.send((f'{str(datetime.today())[11:19]} {iden}: {msg}').encode())
        log.info('Сервер отправляет клиенту ответ...')
        if msg == 'exit':
            IsRunning = False
        else:
            print(f'{str(datetime.today())[11:19]} {iden}: {msg}')
            
    del lst[lst.index(conn)]
    print(f'Пользователь {iden} отсоединился.')
    conn.close()
    




def check_port(port):
    while True:
        try: 
            sock.bind(('', port))
            break
        except:
            port+=1
    log.info(f'Занял порт {port}.') 
    print(f'Занял порт {port}.')
    

def identify(host):
    with open ('users.json',"r") as file:
        userdata = json.load(file)
        if host in userdata:
            return userdata[host]
        else:
            return False
        

log.basicConfig(filename= 'file.log', format='%(levelname)s %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=log.INFO)
log.info('Соединение установлено.')
    
sock = socket.socket()

try:
    port= input("Ваш порт: ")
    if port == '':
        port = 9090
    port = int(port)
    if not 0 <= port <= 65535:
        raise ValueError
except ValueError:
		port = 9090
        
check_port(port)

log.info(f'Сервер подключился к порту - {port}')
sock.listen(1)
log.info('Сервер ожидает подключения ...')



msg = ''
lst = []

while True:
    conn, addr = sock.accept()
    lst.append(conn)
    log.info(f'Клиент {addr} подключился к серверу.')
    t = Thread(target = workwithusers, args = (conn,addr))
    t.start()

    
    
    
log.info('Соединение завершено.')


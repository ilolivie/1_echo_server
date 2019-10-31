import socket
import logging as log

log.basicConfig(filename= 'file.log', format='%(levelname)s %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=log.INFO)
log.info('Соединение установлено.')

sock = socket.socket()
sock.bind(('', 9090))
log.info('Сервер подключился к порту - 9090')
sock.listen()
log.info('Сервер ожидает подключения ...')


conn, addr = sock.accept()
log.info(f'Клиент {addr} подключился к серверу.')
msg = ''
IsRunning = True    
while IsRunning:
    
    data = conn.recv(1024)
    msg = data.decode()
    
    log.info('Сервер отправляет клиенту ответ...')
    if msg == 'exit':
        IsRunning = False
    else:
        print(msg)
        conn.send(msg.encode())
        
conn.close()
    
    
    
log.info('Соединение завершено.')

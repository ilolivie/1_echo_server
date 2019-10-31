import socket
import logging as log

log.basicConfig(filename= 'file.log', format='%(levelname)s %(asctime)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=log.INFO)
log.info('Соединение установлено.')
    
sock = socket.socket()

try:
	port=int(input("Ваш порт: "))
	if not 0 <= port <= 65535:
		raise ValueError
except ValueError:
		port = 9090
        

def check_port(port):
    while True:
        try: 
            sock.bind(('', port))
            break
        except:
            port+=1
    log.info(f'Занял порт {port}.') 
    print(f'Занял порт {port}.')
    
check_port(port)
    



log.info(f'Сервер подключился к порту - {port}')
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

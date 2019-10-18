import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()


conn, addr = sock.accept()
print(addr)
msg = ''
IsRunning = True    
while IsRunning:
    
    data = conn.recv(1024)
    
    msg = data.decode()
    if msg == 'exit':
        IsRunning = False
    else:
        print(msg)
        conn.send(msg.encode())
        
conn.close()
    
    
    
print('конец')

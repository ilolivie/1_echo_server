import socket
from threading import Thread

def scanner(value):
    sock = socket.socket()
    try:
        sock.connect(('localhost',value))
        print(f'Порт {value} открыт.')
        sock.close()
    except OSError:
        pass
lst = []
for i in range(0,10000):
    lst.append(Thread(target = scanner, args = (i,)))
try:
    for i in lst:
        i.start()
    for i in lst:
        i.join()
except RuntimeError:
    pass
       
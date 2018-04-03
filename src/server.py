import socket
from datetime import datetime

PORT = 3000

sock = socket.socket(
    socket.AF_INET,
    socket.SOCKET_STREAM,
    socket.IPPROTO_TCP
)
sock.bind(('127.0.0.1', 3000))
sock.listen()
recv_buffer = 8

while True:
    try:
        conn, addr = sock.accept()
        message = 'We have lift off'

        while True:
            part = conn.recv(recv_buffer)
            message = '[{}] Echoed: 'format(dt.now()) + message
            if len(part) < recv_buffer:
                break
      
conn.close()
sock.close()

import socket
from datetime import datetime

sock = socket.socket(
    socket.AF_INET,
    socket.SOCKET_STREAM,
    socket.IPPROTO_TCP)
sock
address = ('127.0.0.1', 3000)
buffer_length = *
message_complete = False
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
message = 'thanks for the note'
while not message_complete:
    part = conn.recv(buffer_length)
    print(part.decode('utf8'))
    if len(part) < buffer_length:
        break
conn.close()
sock.close()


PORT = 3000
print('--- Starting server on port {} at {} ---'.format(PORT, dt.now()))

sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP
)

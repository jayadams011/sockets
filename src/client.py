import sys
import socket


avail = socket.getaddrinfo('127.0.0.1', 3000)
stream_info = [i for i in avail if i[1] == socket.SOCK_STREAM][0]
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])

msg = 'This is awesome. I am a client sending data to my server'

client.sendall(msg.encode('utf8'))


buffer_length = 8
msg = ''
while True:
    part = client.recv(buffer_length)
    msg += part.decode('utf8')
    if len(part) < buffer_length:
        break

print(msg)


client.close()

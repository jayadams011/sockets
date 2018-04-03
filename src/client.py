import sys
import socket


avail = socket.getaddrinfo('127.0.0.1', 3000)
stream_info = [i for i in avail if i[1] == socket.SOCK_STREAM][0]
client = socket.socket(*stream_info[:3])
client.connect(stream_info[-1])


client.sendall(message.encode('utf8'))


recv_buffer = 8
message = 'This is awesome. I am a client sending data to my server'
while True:
    part = cleint.recv(buffer_length)
    message += part.decode('utf8')
    if len(part) < recv_buffer:
        break

print(message)


client.close()

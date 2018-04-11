import sys
import socket


def run_client():
    """run client function """
    avail = socket.getaddrinfo('127.0.0.1', 3000)
    stream_info = [i for i in avail if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    message = sys.argv[1:]
    message_to_server = ' '.join(message) 
    client.sendall(message_to_server.encode('utf8'))

    buffer_length = 8
    msg = ''
    while True:
        part = client.recv(buffer_length)
        msg += part.decode('utf8')
        if len(part) < buffer_length:
            break

    print(message)

    client.close()


if __name__ == "__main__":
    run_client()

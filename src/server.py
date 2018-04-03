import socket
from datetime import datetime as dt

PORT = 3000
print('---Starting sever on port {} at {}---'.format(PORT, dt.now()))

with socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_TCP) as sock:

    address = ('127.0.0.1', 3000)
    sock.bind(address)
    sock.listen(1)

    conn, addr = sock.accept()
    msg_complete = False

    msg_from_client = ''

    while not msg_complete:
        part = conn.recv(1024)
        msg_from_client += part.decode('utf8')
        if len(part) < 1024:
            break

    year_day = '2018/12/01'
    t = dt.strptime(year_day, '%Y/%m/%d')
    print('[{}] Echoed: {}'.format(t, msg_from_client))

    print('---Stopping sever on port {} at {}---'.format(PORT, dt.now()))
    conn.sendall(msg_from_client.encode('utf8'))

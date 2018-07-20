import json
import socket

sock_serv = socket.socket()

sock_serv.connect(('localhost', 7777))

result = ""

data3 = {
    "action": "presence",
    "type": "status",
}

s_data = json.dumps(data3)

while True:
    data = sock_serv.recv(1024)
    if len(data) == 0:
        break

    result = data.decode("utf-8")

    sock_serv.send(s_data.encode("utf-8"))

    sock_serv.close()

print(json.loads(result))


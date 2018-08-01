import json
import socket

sock_serv = socket.socket()

sock_serv.bind(('', 7777))

sock_serv.listen(1)

data = {
    "msg": "Hello, my name is Roman",
    "action": "probe"
}

s_data = json.dumps(data)

result = ""

while True:
    client, addr = sock_serv.accept()
    print(f"Получен запрос на соединение от {str(addr)}")

    client.send(s_data.encode("utf-8"))

    data = sock_serv.recv(1024)
    if len(data) == 0:
        break

    result = data.decode("utf-8")

    client.close()

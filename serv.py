import socket
import json
import argparse

OK = {
    "response": 200
}

ERROR = {
    "response": 500
}


def get_response_on_message(data):
    if data["action"] == "presence":
        return json.dumps(OK).encode("utf-8")
    else:
        return json.dumps(ERROR).encode("utf-8")


def mainloop(host, port):
    with socket.socket() as sock:
        sock.bind((host, port))
        sock.listen(2)

        conn, addr = sock.accept()
        while True:

            data = conn.recv(1024)
            if not data:
                continue

            data = json.loads(data.decode("utf-8"))

            print(data)

            conn.send(get_response_on_message(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Server side app')
    parser.add_argument("-a", help="Enter address to listen", default="")
    parser.add_argument("-p", help="Enter port to listen", default=7777, type=int)

    args = parser.parse_args()

    mainloop(args.a, args.p)

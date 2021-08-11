import json
import socket

from core import Request, Response
from calculator.settings import parser

HOST = "127.0.0.1"
PORT = 8080

print("Waiting for connection...\n")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(
            "------------Connection received------------"
            + f"\nIP: {addr[0]}"
            + f"\nPort: {addr[1]}"
            + "\n-------------------------------------------"
        )
        while True:
            data = conn.recv(1024)
            if data:
                req_dict = json.loads(data)
                try:
                    request = Request(
                        action=req_dict.pop("action"),
                        service=req_dict.pop("service", None),
                        params=req_dict.pop("params", None),
                        content=req_dict.pop("content", None),
                    )
                    response = parser.parse_request(request)
                except KeyError:
                    response = Response(None, "CE2")
                conn.sendall(response.serialize().encode("utf8"))
            else:
                print("Connection closed by client.\n")
                break

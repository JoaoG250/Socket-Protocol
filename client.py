import json
import socket

HOST = "127.0.0.1"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    request = input("\nRequest: ")
    if request != "exit":
        try:
            req_json = json.loads(request)
        except json.decoder.JSONDecodeError:
            print("\n::::::Error while decoding JSON::::::")
            continue
        s.sendall(json.dumps(req_json).encode("utf8"))
        data = s.recv(1024)
        res_json = json.loads(data)
        print("\n-------Server response received-------")
        print(json.dumps(res_json, sort_keys=True, indent=4))
        print("--------------------------------------\n")
    else:
        break

s.close()

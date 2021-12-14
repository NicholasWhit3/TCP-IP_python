import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect(("172.25.46.9", 11234))
    while True: 
        command = input()
        data = command
        clientSocket.send(data.encode())
        dataFromServer = clientSocket.recv(1024)
        print(dataFromServer.decode())
        if command == "Stop" or command == "stop":
            clientSocket.close()
            break
except socket.error as e:
    print(str(e))

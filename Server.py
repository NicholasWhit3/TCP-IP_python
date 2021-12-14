import socket
import os
import sys
from threading import Thread
from socketserver import ThreadingMixIn


class ThreadConnection(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[SERVER] Accepted a connection request from %s:%s"%(ip, port))

    def run(self):
        while True:
            
            dataFromClient = clientConnection.recv(1024)
            print("[CLIENT] " + dataFromClient.decode())
            path = os.getcwd()
            dir_list = os.listdir(path)
            for elm in dir_list: #!!!!!
                clientConnection.send(elm.encode())
            clientConnection.send("[SERVER] Data received.".encode())
            if dataFromClient.decode() == "[CLIENT] stop" or dataFromClient.decode() == "[CLIENT] Stop":
                break
            
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    tcpServer.bind(('',11234))
except socket.error as e:
    print(str(e))

threads = []

while True:
    tcpServer.listen(5)
    (clientConnection,(ip, port)) = tcpServer.accept()
    newThread = ThreadConnection(ip,port)
    newThread.start()
    threads.append(newThread)


for thread in threads:
    thread.join()

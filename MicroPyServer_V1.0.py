import socket
from HandleRequests import *
from Variables import *

#Might need to change to usocket

class MicroPyServer:
    
    def __init__(self):
        self._sock = None
        self.handle_request = HandleRequests()
        self.port = Variables.PORT
        self.host = Variables.HOST
        
        
    def start(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((Variables.HOST, self.port))
        self._sock.listen(1)
        
        print(f"Server started on http://{self.host}:{self.port}")
        
        while True:
            client, addr = self._sock.accept()
            request_data = client.recv(4096)
            if request_data:
                self.handle_request.handle_request(client, request_data, addr[0])
            client.close() #Obsolete?


server = MicroPyServer()

server.start()
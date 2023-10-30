import socket
from HandleRequests import *
from Variables import *
#todo Might need to change to usocket

class HttpModule:
    
    def __init__(self):
        self.sock = None
        self.handle_request = HandleRequests()
        self.port = Variables.HTTP_PORT
        self.host = Variables.HOST
        
    def boot(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as self.sock:
                self.sock.bind((self.host, self.port))
                self.sock.listen(1)
                self.acceptIncomingConnections()

        except OSError as e:
            print("An error occured while booting up the HTTPS-Server")
            pass       
        
    def acceptIncomingConnections(self):
        
        while True:
            client, addr = self.sock.accept()
            try:
                request_data = client.recv(4096)
                if request_data:
                    self.protocol = "HTTP"
                    try:
                        self.handle_request.handle_request(client, request_data, addr[0], self.protocol, None)
                    except Exception as e:
                        print("Error: ",e)
                        print("Request might be of type HTTPS")
            except OSError as e:
                print("Error: ", e)
                pass
            finally:
                if(client is not None):
                    client.close()
            
            




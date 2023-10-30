import socket
import ssl
from HandleRequests import *


class HttpsModule:
    
    def __init__(self):
        self.sock = None
        self.handle_request = HandleRequests()
        self.port = Variables.HTTPS_PORT
        self.host = Variables.HOST
        self.ssl_cert = Variables.PATH_TO_SSL_CERTIFICATE
        self.ssl_key = Variables.PATH_TO_SSL_PRIVATE_KEY
        self.secure_client = None #todo remove from self an make new var for every connection
        self.context = None
    
    def boot(self):
        try:
            self.setSSLContext()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as self.sock:
                self.sock.bind((self.host, self.port))
                self.sock.listen(1)
                self.acceptIncomingConnections()

        except OSError as e:
            print("An error occured while booting up the HTTPS-Server")
            print(e)
            pass
        
    def setSSLContext(self):
        self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.context.minimum_version = ssl.TLSVersion.TLSv1_3
        
        self.context.load_cert_chain(self.ssl_cert, self.ssl_key)
            
            
    def acceptIncomingConnections(self):
        while True:
            client, addr = self.sock.accept()
            try:
                self.secure_client = self.context.wrap_socket(client, server_side=True)
                
                ssl_tls_protocol = self.secure_client.version()
                
                request_data = self.secure_client.recv(4096) #todo check bytes | sufficient?
                if request_data:
                    self.protocol = "HTTPS"
                    self.handle_request.handle_request(self.secure_client, request_data, addr[0], self.protocol, ssl_tls_protocol)
            except OSError as e:
                
                print("Error: ", e)
                pass
            finally:
                if(self.secure_client is not None):
                    self.secure_client.close()
                client.close()
                

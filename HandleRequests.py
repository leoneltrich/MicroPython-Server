from Variables import *
from LogAllRequests import * #todo May be removed in Production | you may also remove line 9 and line 13 | client_ip may be removed from all contracts


class HandleRequests:

    def __init__ (self):
        self.log = LogAllRequests()
    
    def handle_request(self, client, request_data, client_ip, protocol, ssl_tls_protocol):
        try:
            request_parts = self.initial_processing(request_data)
            request_type = request_parts[0]
            self.log.log(client_ip, request_type, protocol)
            if(ssl_tls_protocol is not None):
                self.log.logProtocol(ssl_tls_protocol)
            if(request_type=="GET"):
                self.process_get(client, request_parts[1])
        except:
            print("Error handling the request")
            raise
        
    def initial_processing(self, request_data):
        try:
            request_lines = request_data.split(b"\r\n")
            request_line = request_lines[0].decode("utf-8")
            request_parts = request_line.split(" ")
            return request_parts
        except:
            print("Error decoding request")
            raise
    
    def process_get(self, client, requested_path):        
        if(requested_path[-1] == "?" and Variables.FORM_SAFE == True ):
            requested_path = requested_path[:-1]
            
        filetype = requested_path.split(".")[-1]

        if requested_path[-1]=="/" and not self.contains_dot(requested_path):
            filetype = "html"
            path = f"./data{requested_path}index.html"
        elif(filetype not in Variables.COMPATIBLE_FILES and self.contains_dot(requested_path)):
            print(requested_path)
            self.error_415(client)
            return
        else:
            path = f"./data{requested_path}" #todo self. ?
        
        try:
            with open(path, "rb") as file:
                file_content = file.read()
                
                content_length = len(file_content)
                content_length=f"Content-Length: {content_length}\r\n\r\n"
                content_type = f"Content-Type: {Variables.COMPATIBLE_FILES[filetype]}\r\n"

                response = b"HTTP/1.1 200 OK\r\n"
                response += content_type.encode('utf-8')
                response += content_length.encode('utf-8')
                response += file_content
                try:
                    client.send(response)
                except OSError as e:
                    print(f"An error occurred sending the response: {e}")
                finally:
                    client.close()
                self.log.served()

        except OSError as e:
            print("Error:", e)
            self.error_404(client)
        finally:
            client.close()
            
            
    def contains_dot(self, string):
        return "." in string
            
    def error_404(self, client):
        print("ERROR 404 REQUEST FAILED\n")
        response = b"HTTP/1.1 404 Not Found\r\n"
        response += b"Content-Type: text/html\r\n\r\n"
        response += b"<h1>Error 404</h1><p>The resources you requested dont exist</p>"
        client.send(response)
        
    def error_415(self, client):
        print("ERROR 415 REQUEST FAILED\n")
        response = b"HTTP/1.1 404 Not Found\r\n"
        response += b"Content-Type: text/html\r\n\r\n"
        response += b"<h1>Error 415</h1><p>The resources you requested don't exist or are of an unvalid media type</p>"
        client.send(response)
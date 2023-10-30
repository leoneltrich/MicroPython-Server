import time

class LogAllRequests:
    def log(self, client_ip, request, protocol):
        local_time = self.get_time()
        print(f"{local_time} 	{client_ip} SENT {protocol} {request} REQUEST")
        
    def served(self):
        local_time = self.get_time()
        print(f"{local_time} 	REQUEST SERVED SUCCESSFULLY")
        
    def logProtocol(self, protocol):
        local_time = self.get_time()
        print(f"{local_time} 	Negotiated SSL/TLS protocol: {protocol}")
        
    def logServerStart(self, ip, port, protocol):
        local_time = self.get_time()
        server = "HTTP"
        if(protocol=="https"):
            server = "HTTPS"
        print(f"{local_time} 	Starting {server}-Server on {protocol}://{ip}:{port}")
            
    def get_time(self):
        time_tuple = time.localtime()
        year, month, day, hour, minute, second = time_tuple[:6]
        local_time = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(year, month, day, hour, minute, second)
        return local_time
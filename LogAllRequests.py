import time

class LogAllRequests:
    def log(self, client_ip, request):
        local_time = self.get_time()
        print(f"{local_time} CLIENT {client_ip} SENT {request} REQUEST")
        
    def served(self):
        local_time = self.get_time()
        print(f"{local_time} REQUEST SERVED SUCCESSFULLY")
        
        
    def get_time(self):
        time_tuple = time.localtime()
        year, month, day, hour, minute, second = time_tuple[:6]
        local_time = "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(year, month, day, hour, minute, second)
        return local_time
from Variables import *
from HttpsModule import *
from HttpModule import *
from LogAllRequests import LogAllRequests
import _thread
import time
#todo Might need to change to usocket
#todo include no cashe response header in request handler
class Main():
    
    def __init__(self):
        self.https_server = HttpsModule()
        self.http_server = HttpModule()
        self.log = LogAllRequests()
    
    def startHttpsServer(self):
        self.https_server.boot()
        
    def startHttpServer(self):          
        self.http_server.boot()

    
    
    def start(self):
        RUN = True
        while(RUN):
            try:
                if(Variables.HTTP_PORT == Variables.HTTPS_PORT):
                    RUN = False
                    raise Exception("HTTP-Port can not be same as HTTPS-Port")
                if(not Variables.ACCEPT_HTTPS_TRAFFIC and not Variables.ACCEPT_HTTP_TRAFFIC):
                    RUN = False
                    raise Exception("At least one server instance needs to be activated to boot")
            except Exception as e:
                print(e)
                break
            if(Variables.ACCEPT_HTTPS_TRAFFIC and not Variables.ACCEPT_HTTP_TRAFFIC):
                self.log.logServerStart(Variables.HOST, Variables.HTTPS_PORT, "https")
                self.startHttpsServer()
            elif(Variables.ACCEPT_HTTPS_TRAFFIC and Variables.ACCEPT_HTTP_TRAFFIC):
                self.log.logServerStart(Variables.HOST, Variables.HTTPS_PORT, "https")
                _thread.start_new_thread(self.startHttpsServer, ())
                
            if(Variables.ACCEPT_HTTP_TRAFFIC):
                self.log.logServerStart(Variables.HOST, Variables.HTTP_PORT, "http")
                self.startHttpServer()
                


server = Main()
server.start()
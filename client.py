import socket
import pickle

class Network:                                                  #setting up netrwork for client and server
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.153"         #make sure this is ip address of the server who is hosting it
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        # print(self.pos)

    def getP(self):                                             #get player object
        return self.p

    def connect(self):                                          #connect to server/returns player object initial
        try:
            self.client.connect(self.addr) 
            return pickle.loads(self.client.recv(2048))
        except: 
            pass   

    def send(self, data):                                       #sending player object and reciving other player object
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
    def set_server(self, serv):
        self.server = serv

#TEST
 # n = Network()
# # print(n.send("hello World"))
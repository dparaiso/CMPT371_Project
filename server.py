import socket
from _thread import *
import pickle
import sys
from utils import *
from Player import player



                                                                        #setting server with local IP


server = "10.0.0.218"  # local IP address
port  = 5555
print (socket.gethostname())  #LAPTOP-GOULBU1Q
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('0.0.0.0', port))   #server,port                                   #binding port and server

except socket.error as e:
    str(e)

s.listen(5)                                                             #starts listining/ open for clinets to connect upto 5
print("Waiting for connection, Server Started")


                                                                        #Player object initialzation
players = [player((2,2),RED,None,0), player((2,2),GREEN,None,0)]


                                                                        #creating client for each thread with different player
def threaded_client(conn, Nplayer):
    conn.send(pickle.dumps(players[Nplayer]))                           #sends inital player object
    reply = ""
    while True:
        try: 
            data = pickle.loads(conn.recv(2048))                        #revice player object from connection
            players[Nplayer] = data 

            if not data:                                                #not data, break and print disconenct
                print("Disconnected")
                break
            else:
                if Nplayer == 1:                                        #setting correct player object for reply
                    reply = players[0]
                else:
                    reply = players[1]

                # print("Received:" , data)
                # print("sending :", reply)


            conn.sendall(pickle.dumps(reply))                           #send player object

        except:
            break  

    print("Lost Connection") 
    conn.close()     


currentPlayer = 0
while True:                                                             #Waitng for connection
    conn, addr = s.accept()                                             #accepts the connection and creates thread for parallel process
    print("Connected to: ", addr)
    
    
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1



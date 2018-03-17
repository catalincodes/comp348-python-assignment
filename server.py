# first of all import the socket library
import socket               
import readfile
import sys
import json

dbaseTuple = readfile.loadFile("data.txt")
jsonPackage = json.dumps({'data':dbaseTuple})
dataSize = sys.getsizeof(dbaseTuple)
print(dataSize)
print(dbaseTuple)
# next create a socket object
# exit()

s = socket.socket()         
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 9999                

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)     
print("socket is listening")            

# a forever loop until we interrupt it or 
# an error occurs
numConn = 0
while numConn == 0:
   # Establish connection with client.
   c, addr = s.accept()     
   numConn = numConn + 1
   print('Got connection from', addr)

   # send a thank you message to the client. 
   
   # c.send('Thank you for connecting'.encode('utf-8'))
   c.send(jsonPackage.encode('utf-8'))
   # Close the connection with the client
   c.close() 
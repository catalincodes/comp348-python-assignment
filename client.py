# Import socket module
import socket
import json               

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 9999             

# connect to the server on local computer
s.connect(('127.0.0.1', port))

s.send("find|John".encode('utf-8'))
returned = s.recv(1024)
returned = returned.decode('utf-8')
print(returned)

# receive data from the server
# receivedJSON = s.recv(1024)
# receivedJSON = receivedJSON.decode('utf-8')
# dataDictionary = json.loads(receivedJSON)
# data = dataDictionary["data"]
# print(data[0][0])
# close the connection
s.close()    
# Import socket module
import socket
import json
import os

def clearScreen():
    if os.name is 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return

def displayMainMenu():
    userChoice = ''
    while True:
        clearScreen()
        print()
        print(' * * * * * * * * * * * * * * * *')
        print(' * Python DB MENU              *')
        print(' * * * * * * * * * * * * * * * *')
        print(' * 1. Find customer            *')
        print(' * 2. Add customer             *')
        print(' * 3. Delete customer          *')
        print(' * 4. Update customer age      *')
        print(' * 5. Update customer address  *')
        print(' * 6. Update customer phone    *')
        print(' * 7. Print report             *')
        print(' * 8. Exit                     *')
        print(' * * * * * * * * * * * * * * * *')
        userChoice = input(' * ')
        
        nrUserChoice = 0
        if userChoice.isnumeric() is True:
            nrUserChoice = int(userChoice)
        else:
            continue
        if (nrUserChoice <= 8) and (nrUserChoice >= 1):
            return nrUserChoice
        else:
            continue
    # return userChoice #should never happen

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 9999             

userChoic = displayMainMenu()
print(userChoic)
userChoice = 'find|john'


# connect to the server on local computer
s.connect(('127.0.0.1', port))

s.send(userChoice.encode('utf-8'))
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
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

def processCommand(userChoice):
    command = ''
    if userChoice is 1:
        command = findCommand()
    elif userChoice is 2:
        command = 'user wants to add a customer'
    elif userChoice is 3:
        command = 'user wants to delete a customer'
    elif userChoice is 4:
        command = 'user wants to update a customer\'s age'
    elif userChoice is 5:
        command = 'user wants to update a customer\'s address'
    elif userChoice is 6:
        command = 'user wants to update a customer\'s phone number'
    elif userChoice is 7:
        command = 'user wants to print a report with all the entries'
    elif userChoice is 8:
        command = 'user wants to exit'
    print(command)
    return
        
def findCommand():
    command = ''
    clearScreen()
    print()
    print(' * * * * * * * * * * * * * * * *')
    print(' * Find customer :             *')
    print(' * * * * * * * * * * * * * * * *')
    name = ''
    while name == '':
        name = input(' * Name: ')
        if name is '':
            print(' * You must provide a name, please try again')
    command = 'find|' + name
    return command 

# Create a socket object
s = socket.socket()         

# Define the port on which you want to connect
port = 9999             

userChoice = displayMainMenu()
print(processCommand(userChoice))
command = 'find|john'


# connect to the server on local computer
s.connect(('127.0.0.1', port))

#send command
s.send(command.encode('utf-8'))

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
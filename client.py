# Import socket module
import socket
import json
import os
import time

isRunning = True


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
    global isRunning
    if userChoice == 1:
        command = findCommand()
    elif userChoice == 2:
        command = addCommand()
    elif userChoice == 3:
        command = 'user wants to delete a customer'
    elif userChoice == 4:
        command = 'user wants to update a customer\'s age'
    elif userChoice == 5:
        command = 'user wants to update a customer\'s address'
    elif userChoice == 6:
        command = 'user wants to update a customer\'s phone number'
    elif userChoice == 7:
        command = 'user wants to print a report with all the entries'
    elif userChoice == 8:
        command = 'exit'
        isRunning = False
    return command
        
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
        if name == '':
            print(' * You must provide a name, please try again')
    command = 'find|' + name
    return command 

def addCommand():
    command = ''
    clearScreen()
    print()
    print(' * * * * * * * * * * * * * * * *')
    print(' * Add new customer :             *')
    print(' * * * * * * * * * * * * * * * *')

    name = ''
    while name == '':
        name = input(' * Enter name: ')
        if name == '':
            print(' * You must provide a name. Please try again')
    age = ''
    while age == '':
        age = input(' * Enter age: ')
        if age == '' or age.isnumeric == False:
            print(' * You must provide a valid age. Please try again')
    address = ''
    while address == '':
        address = input(' * Enter address: ')
        if address == '':
            print(' * You must provide a valid address. Please try again')
    phoneNr = ''
    while phoneNr == '':
        phoneNr = input(' * Enter phone number: ')
        if phoneNr == '':
            print(' * You must provide a valid phone number. Please try again')
    
    #(add|<name>|<age>|<address>|<phone>) 
    command = 'add|' + name + '|' + age  + '|' + address + '|' + phoneNr
    return command
    
def sendRequest(requestedCommand):
    # Create a socket object
    s = socket.socket()         

    # Define the port on which you want to connect
    port = 9999             

    # command = 'find|john'


    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    #send command
    s.send(requestedCommand.encode('utf-8'))

    returned = s.recv(1024)
    returned = returned.decode('utf-8')
    print(returned)
    input("Press Enter to continue...")

    # receive data from the server
    # receivedJSON = s.recv(1024)
    # receivedJSON = receivedJSON.decode('utf-8')
    # dataDictionary = json.loads(receivedJSON)
    # data = dataDictionary["data"]
    # print(data[0][0])
    # close the connection
    s.close()    

def executeProgramLoop():

    while isRunning == True:
        userChoice = displayMainMenu()
        processed = processCommand(userChoice)
        if processed != 'exit':
            sendRequest(processed)
        else:
            print (' * ')
            print (' * ')
            print (' * ')
            print (' * * * * * * *')
            print ('  Good Bye!  *')

    
executeProgramLoop()
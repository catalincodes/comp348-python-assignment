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
    if userChoice == 1:
        command = findCommand()
        sendRequest(command)
    elif userChoice == 2:
        command = addCommand()
        sendRequest(command)
    elif userChoice == 3:
        command = 'user wants to delete a customer'
    elif userChoice == 4:
        command = 'user wants to update a customer\'s age'
    elif userChoice == 5:
        command = 'user wants to update a customer\'s address'
    elif userChoice == 6:
        command = 'user wants to update a customer\'s phone number'
    elif userChoice == 7:
        dbase_asDict = getAllData()
        print (type(dbase_asDict))
        printCommand(dbase_asDict)
        command = 'user wants to print a report with all the entries'
    elif userChoice == 8:
        exitCommand()
    return
        
def findCommand():
    command = ''
    # clearScreen()
    print(' * ')
    print(' * ')
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
    # clearScreen()
    print(' * ')
    print(' * ')
    print(' * * * * * * * * * * * * * * * *')
    print(' * Add new customer :          *')
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

# def deleteCommand():
#    return

def getAllData():
    # Create a socket object
    s = socket.socket()         

    # Define the port on which you want to connect
    port = 9999  

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    #send command
    s.send('getAllData|'.encode('utf-8'))

    receivedJSON = s.recv(1024)
    receivedJSON = receivedJSON.decode('utf-8')
    unpackedJSON = json.loads(receivedJSON)
    data = unpackedJSON["data"]
    return data

def generateTable(dbase_asDict):
    table = list()
    for myKey in dbase_asDict.keys():
        value = dbase_asDict[myKey]
        newLine = [myKey, value[0], value[1], value[2]]
        table.append(newLine)
    return table

def computeColSizes(table):
    colSizes = list()
    for i in range(0, len(table[0])):
        max = 0
        for j in range(0, len(table)):

            if ( len( table[j][i] ) > max ):
                max = len(table[j][i])
        colSizes.append(max+1)
    return colSizes

def computeRowSize(colSizes):
    rowSize = 0
    for currentRow in colSizes:
        rowSize = rowSize + currentRow
    return rowSize + 9


def printCommand(dbase_asDict):
    table = generateTable(dbase_asDict)
    colSizes = computeColSizes(table)
    rowSize = computeRowSize(colSizes)
    
    clearScreen()

    print('/', end='', flush=True)
    for _ in range(rowSize-2):
        print('-', end='', flush=True)
    print("\\")


    print('|', end='', flush=True)
    print('Name'.center(colSizes[0]), end='', flush=True)
    print(' |', end='', flush=True)
    print(' Age'.center(colSizes[1]), end='', flush=True)
    print(' |', end='', flush=True)
    print('Address'.center(colSizes[2]), end='', flush=True)
    print(' |', end='', flush=True)
    print('Phone #'.center(colSizes[3]), end='', flush=True)
    print(' |')

    print('|', end='', flush=True)
    for _ in range(rowSize-2):
        print('-', end='', flush=True)
    print("|")


    for i in range(0, len(table)):
        print('|', end='', flush=True)
        print(table[i][0].rjust(colSizes[0]), end='', flush=True)
        print(' |', end='', flush=True)
        print(table[i][1].rjust(colSizes[1]), end='', flush=True)
        print(' |', end='', flush=True)
        print(table[i][2].rjust(colSizes[2]), end='', flush=True)
        print(' |', end='', flush=True)
        print(table[i][3].rjust(colSizes[3]), end='', flush=True)
        print(' |')

    print("\\", end='', flush=True)
    for _ in range(rowSize-2):
        print('-', end='', flush=True)
    print("/")
    print('')
    input(" Press Enter to continue...")

    #print(rowSize) 
    

def exitCommand():
    global isRunning
    print (' * ')
    print (' * ')
    print (' * ')
    print (' * * * * * * *')
    print ('  Good Bye!  *')
    isRunning = False

def sendRequest(requestedCommand):
    # Create a socket object
    s = socket.socket()         

    # Define the port on which you want to connect
    port = 9999             

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    #send command
    s.send(requestedCommand.encode('utf-8'))

    returned = s.recv(1024)
    returned = ' * ' + returned.decode('utf-8')
    print(returned)
    print(' * ')
    input(" * Press Enter to continue...")

    # receive data from the server
    
    # data = dataDictionary["data"]
    # print(data[0][0])
    # close the connection
    s.close()    

def executeProgramLoop():
    while isRunning == True:
        userChoice = displayMainMenu()
        processCommand(userChoice)

#dbase_asDict = getAllData()
#printCommand(dbase_asDict)

executeProgramLoop()
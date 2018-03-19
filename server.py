import socket               
import readfile
import sys
import json
import time

# References: boiler-plate code for connection to server 
    
def loadDatabase():
    dbaseList = readfile.loadFile("data.txt")
    dbase_asDict = readfile.processListToDict(dbaseList)
    return dbase_asDict

# packing a dbase into JSON

# dataSize = sys.getsizeof(dbaseTuple)

def executeServerLoop():
    # create a socket object
    s = socket.socket()         

    # reserve port 9999 
    port = 9999                

    # bind to the port
    s.bind(('', port))        

    # put the socket into listening mode
    s.listen(5)     
    # print("socket is listening")            

    # a forever loop until we interrupt it or 
    # an error occurs

    print("Server is listening for commands: ")

    while True:
        # Establish connection with client.
        c, _ = s.accept()  
        # print('Got connection from', addr)
        # print('Waiting for command: ...')

        encodedCommand = c.recv(1024)
        command = encodedCommand.decode('utf-8')
        # print (command)
        parsedCommand = command.split('|')

        
        # print (parsedCommand)
        response = processCommand(parsedCommand)
        
        c.send(response.encode('utf-8'))
        
        # c.send(jsonPackage.encode('utf-8'))
        # Close the connection with the client
        c.close() 

def processCommand(newCommand):
    UNRECONGIZED_COMMAND = 'Unrecognized Command'
    response = ''
    
    if  len(newCommand) == 2 : #it's either find, delete or getAllData
        if newCommand[0] == 'find':
            print(str(time.ctime()) + ' - ' + 'Find command')
            foundEntry = find(newCommand[1])
            if foundEntry == None:
                response = 'Server response: ' + newCommand[1] + ' not found in database'
            else:
                response = 'Server response: ' +  foundEntry[0] + '|' + foundEntry[1] + '|' + foundEntry[2] + '|' + foundEntry[3]
        
        elif newCommand[0] == 'delete':
            print(str(time.ctime()) + ' - ' + 'Delete command')
            response = delete(newCommand[1])
        
        elif newCommand[0] == 'getAllData':
            print(str(time.ctime()) + ' - ' + 'GetAllData command')
            response = json.dumps({'data':dbase_asDict})
            # response = jsonPackage.encode('utf-8')
        
        else:
            print(str(time.ctime()) + ' - ' + 'Unknown command')
            response = UNRECONGIZED_COMMAND
    
    elif len(newCommand) == 3 :
        print(str(time.ctime()) + ' - ' + 'Unknown command')
        response = UNRECONGIZED_COMMAND
    
    elif len(newCommand) == 4 :

        if newCommand[0] == 'update':
            if (newCommand[2] == 'age'):
                print(str(time.ctime()) + ' - ' + 'Update age command')
                response = updateAge(newCommand[1], newCommand[3])
            elif (newCommand[2] == 'address'):
                print(str(time.ctime()) + ' - ' + 'Update address command')
                response = updateAddress(newCommand[1], newCommand[3])
            elif (newCommand[2] == 'phone'):
                print(str(time.ctime()) + ' - ' + 'Update phone number command')
                response = updatePhone(newCommand[1], newCommand[3])
            else:
                print(str(time.ctime()) + ' - ' + 'Unknown command')
                response = UNRECONGIZED_COMMAND
        
        else:
            print(str(time.ctime()) + ' - ' + 'Unknown command')
            response = UNRECONGIZED_COMMAND

    elif len(newCommand) == 5 :

        if newCommand[0] == 'add':
            print(str(time.ctime()) + ' - ' + 'Add new customer command')
            response = add(newCommand[1], newCommand[2], newCommand[3], newCommand[4])
        
        else:
            print(str(time.ctime()) + ' - ' + 'Unknown command')
            response = UNRECONGIZED_COMMAND
    
    else:
        print(str(time.ctime()) + ' - ' + 'Unknown command')
        response = UNRECONGIZED_COMMAND

    return response

def find(name):
    if name in dbase_asDict:
        queryDbase = dbase_asDict[name]
        result = [name, queryDbase[0], queryDbase[1], queryDbase[2]]
    else:
        result = None
    return result

def add(name, age, address, phoneNumber):
    global dbase_asDict
    if name in dbase_asDict:
        result = 'Customer already exists.'
    else:
        dbase_asDict[name] = [age, address, phoneNumber]
        result = 'Customer has been added!'
    return result
    
def delete(name):
    global dbase_asDict
    if name in dbase_asDict:
        dbase_asDict.pop(name, None)
        result = "Customer was removed!"
    else:
        result = "Customer not found."
    return result

def updateAge(name, age):
    global dbase_asDict
    if name in dbase_asDict:
        origEntry = dbase_asDict[name]
        newEntry = [age, origEntry[1], origEntry[2]]
        dbase_asDict[name] = newEntry
        result = "Customer age was updated!"
    else:
        result = "Customer not found."
    return result

def updateAddress(name, address):
    global dbase_asDict
    if name in dbase_asDict:
        origEntry = dbase_asDict[name]
        newEntry = [origEntry[0], address, origEntry[2]]
        dbase_asDict[name] = newEntry
        result = "Customer\'s address was updated!"
    else:
        result = "Customer not found."
    return result

def updatePhone(name, phone):
    global dbase_asDict
    if name in dbase_asDict:
        origEntry = dbase_asDict[name]
        newEntry = [origEntry[0], origEntry[1], phone]
        dbase_asDict[name] = newEntry
        result = "Customer\'s phone number was updated!"
    else:
        result = "Customer not found."
    return result

dbase_asDict = loadDatabase()
executeServerLoop()
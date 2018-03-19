import socket               
import readfile
import sys
import json

    
def loadDatabase():
    dbaseList = readfile.loadFile("data.txt")
    dbase_asDict = readfile.processListToDict(dbaseList)
    return dbase_asDict

# packing a dbase into JSON

# dataSize = sys.getsizeof(dbaseTuple)

def executeServerLoop():
    # create a socket object
    s = socket.socket()         
    print("Socket successfully created")

    # reserve port 9999 
    port = 9999                

    # bind to the port
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
    while True:
        # Establish connection with client.
        c, addr = s.accept()  
        print('Got connection from', addr)
        print('Waiting for command: ...')

        encodedCommand = c.recv(1024)
        command = encodedCommand.decode('utf-8')
        print (command)
        parsedCommand = command.split('|')

        
        print (parsedCommand)
        response = processCommand(parsedCommand)
        
        c.send(response.encode('utf-8'))
        
        # c.send(jsonPackage.encode('utf-8'))
        # Close the connection with the client
        c.close() 

def processCommand(newCommand):
    UNRECONGIZED_COMMAND = 'Unrecognized Command'
    response = ''
    
    if  len(newCommand) == 2 : #it's either find, delete or getAllData
        print ('****')
        print(newCommand[0])
        if newCommand[0] == 'find':
            foundEntry = find(newCommand[1])
            if foundEntry == None:
                response = 'Server response: ' + newCommand[1] + ' not found in database'
            else:
                response = 'Server response: ' +  foundEntry[0] + '|' + foundEntry[1] + '|' + foundEntry[2] + '|' + foundEntry[3]
        
        elif newCommand[0] == 'delete':
            print('delete')
            response = 'delete'
        
        elif newCommand[0] == 'getAllData':
            print('getAllData')
            response = json.dumps({'data':dbase_asDict})
            # response = jsonPackage.encode('utf-8')
        
        else:
            response = UNRECONGIZED_COMMAND
    
    elif len(newCommand) == 3 :
        response = UNRECONGIZED_COMMAND
    
    elif len(newCommand) == 4 :

        if newCommand[0] == 'update':
            print('update') 
            response = 'update'
        
        else:
            response = UNRECONGIZED_COMMAND

    elif len(newCommand) == 5 :

        if newCommand[0] == 'add':
            response = add(newCommand[1], newCommand[2], newCommand[3], newCommand[4])
        
        else:
            response = UNRECONGIZED_COMMAND
    
    else:
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
    

dbase_asDict = loadDatabase()

# response = find('John')
# print(response)
executeServerLoop()
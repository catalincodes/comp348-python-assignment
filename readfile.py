# things to check:
    # DONE! remove \n at end of line
    # TODO: number of elements
    # TODO: are they full
    # TODO: is there a name
    # TODO: are they valid elements ? 

def processListToDict(dbase_asList):
    dbase_asDict = {}
    for entry in dbase_asList:
        dictKey = entry[0]
        dictValue = [entry[1], entry[2], entry[3]]
        dbase_asDict[dictKey] = dictValue
    return dbase_asDict

def loadFile(filename):
    dbase_asList = []
    with open(filename, "r") as file:
        print('Reading file.')
        completeFile = file.readlines()
        print('Processing file.')
        for line in completeFile:
            tokenized = line.split('|') 
            
            #remove '\n' from last entries 
            lastItem = tokenized[len(tokenized) - 1]
            if (lastItem[-1:] is '\n'):
                tokenized[len(tokenized) - 1] = lastItem[:-1]
            
            # remove trailing spaces
            for item in tokenized:
                item.strip()
            
            try:
                age = int(tokenized[1])
            except ValueError:
                print("The following entry does not have a valid age:")
                print(line)
                continue

            age = int(tokenized[1])                     

            #remove invalid entries
            if (len(tokenized) != 4): 
                print("The following entry with more than 4 columns was rejected for being over-zealous:")
                print(line)
                continue
            elif (tokenized[0] == ''):
                print("The following entry does not have a valid name:")
                print(line)
                continue
            elif (age < 0 or age > 199 ):
                print("The following entry does not fit a valid age range.")
                print("I mean really ... you cannot be under 0 years of age or over 200 years old.")
                print(line)
                continue
            else:
                # print('adding ' + tokenized.__str__())
                dbase_asList.append(tokenized)
                
    # dbase_asTuple = tuple(item for item in dbase_asList)
    return dbase_asList


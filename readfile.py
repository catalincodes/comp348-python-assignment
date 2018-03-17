def loadFile(filename):
    dbase_asList = []
    with open(filename, "r") as file:
        completeFile = file.readlines()
        for line in completeFile:
            tokenized = line.split('|') 
            
            
            #remove '\n' from last entries 
            lastItem = tokenized[len(tokenized) - 1]
            if (lastItem[-1:] is '\n'):
                tokenized[len(tokenized) - 1] = lastItem[:-1]
            if (len(tokenized) is not 4): continue

        # things to check:
            # DONE! remove \n at end of line
            # TODO: number of elements
            # TODO: are they full
            # TODO: is there a name
            # TODO: are they valid elements ? 
        print('adding ' + tokenized.__str__())
        dbase_asList.append(tokenized)
    
    dbase_asTuple = tuple(item for item in dbase_asList)
    print(dbase_asTuple)
    return dbase_asTuple


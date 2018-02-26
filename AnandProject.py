import json

with open("/Users/anandchandran/Documents/season7.json") as fileJ:
    d = json.load(fileJ)
    hashTable = {'Test': [1, 2, 3]}
    for iterator in range(1, 25, 1):
        iteratorString = 'Episode ' + str(iterator)
        ep1Array = d[iteratorString]
        for i in range(0, 4, 1):
            investors = ep1Array[i]['investors']
            if " and " not in investors:
                individualInvestors = investors.split(", ")
                # print(individualInvestors)
                for v in individualInvestors:
                    # print(v)
                    if not v:
                        pass
                    else:
                        if v in hashTable:
                            print "Extract List"
                            extractedList = hashTable[v]
                            extractedList.append(ep1Array[i]['company']['title'])
                            hashTable[v] = extractedList
                        else:
                            print "Assign New List for " + v
                            newList = [ep1Array[i]['company']['title']]
                            hashTable[v] = newList
            else:
                individualInvestors = investors.split(" and ")
                for v in individualInvestors:
                    # print(v)
                    if not v:
                        pass
                    else:
                        if v in hashTable:
                            print "Extract List"
                            extractedList = hashTable[v]
                            extractedList.append(ep1Array[i]['company']['title'])
                            hashTable[v] = extractedList
                        else:
                            print "Assign New List for " + v
                            newList = [ep1Array[i]['company']['title']]
                            hashTable[v] = newList
    print(hashTable)

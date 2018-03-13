import json
from urllib2 import urlopen

import re


#    d = json.load(fileJ)
data = urlopen("https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json")
data = data.read()
data = str(data)
data = data.replace("\\n",'')
d = json.loads(data)
#clean the json data
#for line in fileJ:
#data.append()
#initialize a random dictionary with some data
hashTable = {'Test': [1, 2, 3]}
#countTable={'Test':[1,2,3]}
count=0
for iterator in range(1, 25, 1):  # Iterate for all 24 Episodes in the Json Object
    iteratorString = 'Episode ' + str(iterator)
    ep1Array = d[iteratorString]
    for i in range(0, 4, 1):  # Iterate through the 4 Json Objects in the Json Array
        investors=re.sub("[^a-zA-Z,]", " ",ep1Array[i]['investors'])#
        investors=investors.replace("  "," ")

        #investors = ep1Array[i]['investors']
        if "and" not in investors and "," not in investors:  # Investor Split Logic

            individualInvestors = investors.split(", ")
            for v in individualInvestors:
                if not v:
                    pass
                else:
                    if v in hashTable:
                        extractedList = hashTable[v]  # If key is found then extract and append the company
                        extractedList.append(ep1Array[i]['company']['title'])
                        hashTable[v] = extractedList
                    else:
                        newList = [ep1Array[i]['company']['title']]
                        hashTable[v] = newList  # If key is not found then create a new list and assign as the
                        # value to the investor
        else:

            individualInvestors = investors.replace(" and ", ", ").split(", ")

            for I in range(len(individualInvestors)):
                individualInvestors[I]=individualInvestors[I].replace(",","")


            for v in individualInvestors:
                if not v:
                    pass
                else:
                    if v in hashTable:
                        extractedList = hashTable[v]
                        extractedList.append(ep1Array[i]['company']['title'])
                        hashTable[v] = extractedList
                    else:
                        newList = [ep1Array[i]['company']['title']]
                        hashTable[v] = newList
hashTable.__delitem__('Test')  # Delete the test Detail.
print "\n-----------------------------INVEST DETAILS ------------------------------------------\n"
print(hashTable)  # Print the dictionary which contains the investment details
print "\n------------------SORTED ACCORDING TO NO. OF INVESTMENTS------------------------------\n"
for k in sorted(hashTable, key=lambda k: len(hashTable[k]), reverse=True):  # Sort Logic
    print(k,hashTable[k])
    print("\n")
print "\n--------------------------------------------------------------------------------------\n"
print count

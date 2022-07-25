import time
import re
import json

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def PrintList(self):
        printval = self.head
        while printval != None:
            print(printval.data)
            printval = printval.next

def Parser(LogPath, Match):
    with open(LogPath, 'r') as f:
        while f.readline():
            file = f.readline()
            #print(file[0:10])
            if re.search(Match, file):
                print(file)
                f2 = open(LogPath+'filtered', 'a')
                f2.write(file)
                f2.close()
 
def ipChecker(InputIP):
    count = 0
    for i in InputIP.split('.'):
        if (int(i)<255) and (int(i)>=0) and ((int(i[0]) != 0) and (int(i) == 0)):
            count = count + 1
        else:
            print("invalid Ipv4")
            exit()
    if count < 5:
        print("Valid Ipv4")
    else:
        print("invalid Ipv4")

def LogParse2(LogPath):
    '''Find runtime for each process in the log'''
    logData = {}
    
    with open(LogPath, 'r') as f:
        while f.readline():
            line = f.readline()
            #print(line)
            #match = re.search("[a-zA-Z_]+\.\w+", line)
            match = re.search("url_helper.py", line)
            if match != None:
                #print(match.group(0))
                filename = match.group(0)
                logData[line[7:14]] = {"FileName":filename}
    with open('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/cloud-init-files', 'w') as f:
        #f.write(str(logData))
        for entry in logData:
            f.write(json.dumps(entry, indent = 4))
        f.close()

def LogParse3(LogPath):
    dict01 = {}
    mylist = LinkedList()
    iterator = 0
    with open(LogPath, 'r') as f:
        while f.readline():
            line = f.readline()
            split = line.split(' ')
            #print(split)
            if iterator == 0:
                mylist.head = Node(split)
                iterator += 1
            else:
                mylistItr = Node(split)
                iterator += 1
'''    mylist.head.next = mylistItr1
    for i in range(1,len(iterator)):
        mylistItr+str(i-1).next = mylistItr[i]
        
    mylist.PrintList()
'''            
            

#dict02 = {"TimeStamp":{"InstanceID":"i-sfasda2", "VolumeMapping":{"root":"xvda1", "Secondary":"xvda2"}, "Subnet":"sub-23232"}}
#print(dict02['TimeStamp']["VolumeMapping"].get("root"))
    
#LogParse3('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/cloud-init.log')   

list01 = ['ab', 'cd', 'ef', 'gh', 'ij']
iterator = 0

dict01 = {}

for i in list01:
    dict01[i] = iterator
    iterator += 1
print(dict01)

print(dict01.get('gh'))

for k,v in dict01.items():
    print(k)


#ipChecker('192.168.0.225')
#dict01 = {"22:30:52":{"InstanceID":"i-2434312tts",{"VolumeMapping":{"root":"xvda1","Secondary":"xvda2"}},{"Subnet":"sub-34242sdv"}}}


''' Lookup for Interview 
file_name = "log.txt"
file = open(file_name, "r")
data = []
order = ["date", "url", "type", "message"]

for line in file.readlines():
    details = line.split("|")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)
    
for entry in data:
    print(json.dumps(entry, indent = 4))
'''
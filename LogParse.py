import time
import re
import json

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

dict02 = {"TimeStamp":{"InstanceID":"i-sfasda2", "VolumeMapping":{"root":"xvda1", "Secondary":"xvda2"}, "Subnet":"sub-23232"}}
print(dict02['TimeStamp']["VolumeMapping"].get("root"))
    
#LogParse2('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/cloud-init.log')   
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
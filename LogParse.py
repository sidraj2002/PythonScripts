import time
import re 

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
            match = re.search("[a-zA-Z_]+\.\w+", line)
            if match != None:
                #print(match.group(0))
                filename = match.group(0)
                logData[line[7:14]] = {"FileName":filename}
    with open('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/cloud-init-files', 'w') as f:
        f.write(str(logData))
        f.close()
    
        
LogParse2('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/cloud-init.log')   
#ipChecker('192.168.0.225')


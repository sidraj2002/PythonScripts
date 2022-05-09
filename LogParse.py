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
        if (int(i)<255) and (int(i)>=0) and ((int(i[0]) == 0) and (int(i) == 0)):
            count = count + 1
        else:
            print("invalid Ipv4")
            exit()
    if count < 5:
        print("Valid Ipv4")
    else:
        print("invalid Ipv4")
#Parser('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/testlog2', '35.172.155.192')   
ipChecker('192.168.0.225')
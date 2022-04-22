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
                
        
Parser('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/testlog2', '35.172.155.192')   
from datetime import datetime
import random
import string
import time
from random import choice
from datetime import datetime, date, time, timedelta

def ReverseString(InputString):
    reverseString = {}
    count = 0
    print(count)
    while count <= len(InputString):
        for i in InputString:
            #print(InputInteger)
            #print(i)
            reverseString[count] = i
            count = count+1
    for i in range(len(InputString),0,-1):
        print(reverseString[i])
    return(True)

def Palindrom(InputString):
    output = False
    count = 0
    dict = {}
    for i in InputString:
        dict[count] = i
        count = count+1
    for i in InputString:
        #print(i)
        for j in range(len(InputString)-1,0,-1):
            if i != dict[j]:
                print(dict[j])
                return(False)
                
    
    return(True)
    
def Palindrom2(InputString):
    if InputString == InputString[::-1]:
        return True
    else:
        return False
        
def ReverseString2(InputString):
    str = reversed(InputString)
    for i in str:
        print(i)
        
def BubbleSort(Input):
    x = 0
    dict = {}
    count = 0
    for i in Input:
        dict[count] = i
    for i in range(len(Input)-1,0,-1):
        for j in range(i):
            if Input[j] > Input[j+1]:
                x = Input[j]
                Input[j] = Input[j+1]
                Input[j+1] = x
 
    print(Input)

def RomanAddition(Input):
    count = 0
    DictInput = {}
    for i in Input:
        if i == 'I':
            DictInput[i] = 1
        if i == 'V':
            DictInput[i] =  5
        if i == 'X':
            DictInput[i] = 10
        if i == 'L':
            DictInput[i] = 50
        if i == 'C':
            DictInput[i] = 100
        if i == 'D':
            DictInput[i] = 500
        if i == 'M':
            DictInput[i] = 1000
    print(DictInput)
    iterable = iter(DictInput.values())
    for value in DictInput.values():
        NextVal = next(iterable)
        if (value == 'I' and NextVal == 'V') or (value == 'I' and NextVal =='X'):
            print(value)
            count = count - value
        if (value == 'X' and NextVal == 'L') or (value == 'X' and NextVal =='C'):
            print(value)
            count = count - value
        if (value == 'C' and NextVal == 'D') or (value == 'C' and NextVal =='M'):
            print(value)
            count = count - value
        else:
            print(value)
            count = count + value
    return count
    
def WordCountString(InputString):
    InputString = InputString+'*' 
    '''Adding trailing character to indicate end of string'''
    count = 0
    dict2 = {}
    j = 0
    x = ''
    
    for i in range(len(InputString)):
        if InputString[i] != '*':
            if (InputString[i] == ' ') and (InputString[i+1] != ' '):
                count = count + 1
                dict2[j] = x
                x = ''
                j = j + 1
            if (InputString[i]) != ' ':
                x = x + InputString[i]
    j = j+1
    dict2[j] = x
    print(dict2.values().index('Anu'))
    return count,dict2    

def LongestNonRepeatingString(InputString):
    outputString = InputString[0]
    for i in InputString:
        for j in range(1,len(InputString)):
            if i == InputString[j]:
                print(j)
                return outputString
            else:
                outputString = outputString + InputString[j]
    return outputString

def longestPalindromSubstring(InputString):
    
    a = InputString
    b = InputString[::-1]
    
    for i in range(len(a)-1):
        for j in range(len(b)-1):
            if (a[i] == b[j]) and (a[i+1] == b[j+1]):
                return InputString[i:len(InputString)-j]
            
    return False

def RandomStringGen():
    output = ''
    output = (''.join(random.choice(string.ascii_letters) for i in range(10)))
    return output
    
def DataWriter(InputData):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file = open('/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/testlog.txt', 'a')
    line = InputData + ' ' + dt + '\n'
    file.write(line)
    file.close()
def DataFetcher(Seconds, InputFile):
    dt = datetime.now()
    timeNow = dt.strftime("%Y-%m-%d %H:%M:%S")
    print(timeNow)
    File = open(InputFile, 'r')
    count = 0
    temp = File.readline()
    while temp != '':
        temp = File.readline()
        #temp = temp.reverse()
        print(temp)
    #For count = timeNow[]

def DataWriter2(InputData):
    output = ()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newData = InputData + '/' + dt
    output = tuple([newData],)
    #print(output)
    return output
def DataFetcher2(Period, InputData):
    dt = datetime.now()
    delta = dt + timedelta(seconds=Period)
    for i in InputData:
        split = i[0].split('/')
        if split > delta:
            print(InputData)
        else:
            continue
        
def LongestCommonPrefix(InputArray):
    MyPrefix = ''
    count = 0
    MyArray = iter(InputArray)
    for i in range(len(InputArray[0])):
        item = next(MyArray)
        print(item[count])
        if MyArray[0][i] == item[i]:
            MyPrefix += MyArray[0][i]
            count = count + 1
    print(MyPrefix)

def FindTargetNum(SortedNumList, Target):
    tmp = len(SortedNumList)
    tmp = round(tmp/2)
    #print(tmp)
    #print(SortedNumList[tmp])
    
    if Target >= SortedNumList[tmp]:
        for i in range(tmp,len(SortedNumList),1):
            if SortedNumList[i] == Target:
                print("Found at " + str(i))
                return i
            if (SortedNumList[i] > Target) and (SortedNumList[i+1] < Target):
                return i
    else:
        for i in range(tmp,0,-1):
            if SortedNumList[i] == Target:
                print("Found at " + str(i))
                return i
            if (SortedNumList[i] > Target) and (SortedNumList[i-1] < Target):
                return i
    
#print(ReverseString('abcdefghijk'))
#print(Palindrom2('1211'))
#ReverseString('siddharth')
#BubbleSort([2,5,1,3,5,6])
#print(RomanAddition('III'))
#numberofwords = WordCountString('Hello,    My Name I Anu ')
#print(numberofwords)
#print(LongestNonRepeatingString('pwwkew'))
#print(longestPalindromSubstring('dvd'))
''' File reader / Write '''
#counter = 0
#while counter < 60:
#    rand = RandomStringGen()
#    DataWriter(rand)
#    counter = counter + 1
#    time.sleep(1)
#DataFetcher(10,'/home/ec2-user/environment/Python_Scripts/PythonScripts/testdir/testlog.txt')
'''Data Fetcher Input Code - Come back later 
data = ()
for i in range(60):
    randStr = ''.join(random.choice(string.ascii_letters) for i in range(10))
    data = (data) + tuple([DataWriter2(randStr)])
#print(data)
DataFetcher2(-10, data)
'''
#LongestCommonPrefix(["decreate","dexvd","defefdfd","defdfdg"])
FindTargetNum([1,3,5,6], 2)

'''
Use following:
.join
f.open()
reveresed()
split()
.append()
Stream
read chunks
key,value traversal
O(N) or OlogN optimization
Window approach
'''
'''
string = 'abcdefghijk'
var = list(string)
j = 0
#while j <= len(string)-1:
for i in string:
    print(j)
    var[j] = i
    j = j+1
for i in string:
    print(j)
    var[j-1] = i
    j = j-1
    
print(var)
'''


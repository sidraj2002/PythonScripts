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
    return count+1,dict2    

#print(ReverseString('abcdefghijk'))
#print(Palindrom2('1211'))
#ReverseString('siddharth')
#BubbleSort([2,5,1,3,5,6])
#print(RomanAddition('III'))
numberofwords = WordCountString('Hello,    My Name I Anu ')
print(numberofwords)
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


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
    
#print(ReverseString('abcdefghijk'))
#print(Palindrom2('1211'))
ReverseString('siddharth')
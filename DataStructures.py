class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def ListPrint(self):
        printval = self.head
        while printval != None:
            print(printval.data)
            printval = printval.next
    def PopulateList(self, InputList):
        count = 0
        list = {}
        list[0] = 'x'
        for i in range(0,len(InputList)):
            list[count] = Node('')
            count = count+1
        #print(InputList[0])
        self.head = Node(InputList[0])
        #print(self.head.data)
        #print(list[0])
        self.head.next = list[0]
        #print(self.head.next)
        count = 0
        
        for i in InputList:
                list[count].data = i
                #print(list[count].data)
                
                if count == len(InputList)-1:
                    list[count].next = None
                    
                else:
                    list[count].next = list[count+1]
                    #print(list[count].data)
                    #print(list[count].next)
                    count = count+1
def SumLinkedLists(input0,input1):
    SumDict = {}
    input0 = input0.head.next
    count = 0
    while input0 != None:
        SumDict[count] = input0.data
        count = count+1
        input0 = input0.next
    
    SumDict2 = {}
    input1 = input1.head.next
    count = 0
    while input1 != None:
        SumDict2[count] = input1.data
        count = count+1
        input1 = input1.next
    FinalSum = {}
    count = 0
    #print(SumDict2)
    while count < len(SumDict) and count < len(SumDict2):
        FinalSum[count] = int(SumDict[count]) + int(SumDict2[count])
        #print(FinalSum[count])
        count = count + 1
    return list(FinalSum.values())
    #print(SumDict)
            
class BinaryTree:
    def __init__(self):
        self.head = None
    
    def PopulateTree(self, InputData):
        BT={}
        count = 0
        for i in range(0,len(InputData)):
            BT[i] = Node('')
            while (InputData[i] > 0) and (i==0):
                self.head.data = InputData[i]
            while InputData[i] != '' and i >= 1:
                if InputData[i] > self.head.data:
                    self.head.left = BT[i]
                    break
                else:
                    self.head.right = BT[i]
                    break
        for i in InputData:
            BT[count].data = i
           # if i > 
            
            
            


#Input = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
#NewList = LinkedList()
#NewList.PopulateList(Input)
#NewList.ListPrint()

''' Sum two Linked Lists '''

Input1 = ('2','4','6','8','12')
Input2 = ('1','3','5','7','9','10','11')
NewList1 = LinkedList()
NewList1.PopulateList(Input1)
NewList2 = LinkedList()
NewList2.PopulateList(Input2)


Input3 = {}
Input3 = SumLinkedLists(NewList1,NewList2)
#print(Input3)
NewList3 = LinkedList()
NewList3.PopulateList(Input3)
NewList3.ListPrint()
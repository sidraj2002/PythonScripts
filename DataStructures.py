class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
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
            
        
        
            
'''list1 = LinkedList()
list1.head = Node('Monday')
l2 = Node('Tuesday')
l3 = Node('Wednesday')
list1.head.next=l2
l2.next=l3'''

Input = 'abcdefgh'
NewList = LinkedList()
NewList.PopulateList(Input)
NewList.ListPrint()

    
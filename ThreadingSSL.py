import ssl, socket
import threading

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        print(ssock)
        
def CountRepeatWords(InputString):
    myList = InputString.split()
    myDict = {}
    for i in myList:
        count = myList.count(i)
        myDict[i] = count
    #print(myDict)
    return myDict
def LargestOccurence(mydict):
    mydict = sorted(mydict.items(),reverse=True)
    print(mydict)

class mythread:
    def __init__(self):
        self.name = None
    def StartThread(self, function):
        info = {'stop': False}
        thread = threading.Thread(target=function, args=(info,))
        return thread
    def StopThread(self, thread):
        thread.join()
 
def ThreadingExample(FunctionName):
    thread = threading.Thread(target=FunctionName)
    thread.start()
    #print(thread.name)
#CountRepeatWords('Hello My Name Earl My')
#print(LargestOccurence(CountRepeatWords('Hello My Name Name Name Earl My My My My')))

#count = '0'
#NewThread = mythread()
#NewThread.name = 'Thread'+count

#MyThread = NewThread.StartThread(CountRepeatWords('Hello My Name Name Name Earl My My My My'))
#print(MyThread)
#NewThread.StopThread(MyThread)

ThreadingExample(CountRepeatWords('Hello My Name Name Name Earl My My My My'))
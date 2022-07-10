import json
import threading
import time

plans = {}
plans = {
  "planId": "BASIC",
  "monthlyCost": "9.99"
}, {
  "planId": "STANDARD",
  "monthlyCost": "49.99"
}, {
  "planId": "PREMIUM",
  "monthlyCost": "249.99"
}

class Customer:
    def __init__(self, Data):
        self.customerID = Data.get("CustomerID")
        self.products = [{"productName": Data.get("ProductName"), "subscriptionID": Data.get("PlanID"),
        "subscriptionStartDate":''}]
        
def newCust(CustID):
    data = {}
    if CustID == None:
        print("Error: Empty CustomerID")
    else:
        data = {"CustomerID":CustID}
    customer = Customer(data)
    return customer

def addProduct(customer, Product, PlanID):
    if customer.products == None:
        print('No existing Products Found: Continue to add products')
        
#mycust01 = newCust('Sid01')
#print(mycust01.customerID)

''' New Section - Singleton + Threading ''' 

class Singleton():
    __instance = None
    
    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
            return Singleton.__instance
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Cannot instantiate Singleton more than once")
        else:
            Singleton.__instance = self
    def printVal(self):
        print(self.__instance)
            
X = Singleton.get_instance()
print(X)
X.__instance = 'Sid01'
print(X.__instance)
X.__instance = 'Sid02'
print(X.__instance)

class ParallelThreads(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.name = name

    def run(self, sleep=5):
        print('Starting thread', self.name)
        time.sleep(sleep)
        print('Finished thread', self.name)

thread01 = ParallelThreads(1, 'Thread01', 1)
thread02 = ParallelThreads(1, 'Thread02', 2)

thread01.start()
thread02.start()


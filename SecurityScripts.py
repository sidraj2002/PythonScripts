import time

def ExponentialBackoff(count):
        
    if count > 0:
        time.sleep(count*2)
    


count = 0
Userinput = ''
while (Userinput != "Admin") and (count < 10):
    print("Please Enter DoB:\n")
    Userinput = input()
    print("Wrong Input")
    ExponentialBackoff(count)
    count = count + 1
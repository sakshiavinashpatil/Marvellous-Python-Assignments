import threading

def DisplayEven():
    #print("Inside DisplayEven")
    EvenList = []
    for i in range(2,21,2):
        EvenList.append(i)
    print("Even numbers : ",EvenList)

def DisplayOdd():
    #print("Inside DisplayOdd")
    OddList = []
    for i in range(1,20,2):
        OddList.append(i)
    print("Odd numbers : ",OddList)

def main():
    #print("Inside Main")
    Even_T1 = threading.Thread(target=DisplayEven)      #Creation of Thread
    Even_T1.start()                                     #To start the Thread
    Even_T1.join()

    Odd_T2 = threading.Thread(target=DisplayOdd)        #Creation of Thread
    Odd_T2.start()                                      #To start the Thread
    Odd_T2.join()

if __name__ =="__main__":
    main()
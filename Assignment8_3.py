import threading

def AddEven(input_list):
    #print("Inside AddEven")
    EvenList = []
    for i in input_list:
        if i % 2 == 0:
            EvenList.append(i)
    print("Even numbers : ",EvenList)

    EvenTotal = 0
    for num in EvenList:
        EvenTotal = EvenTotal + num
    print("Sum of Even Numbers in provided list : ",EvenTotal)

def AddOdd(input_list):
    #print("Inside AddOdd")
    OddList = []
    for i in input_list:
        if i % 2 != 0:
            OddList.append(i)
    print("Odd numbers : ",OddList)

    OddTotal = 0
    for num in OddList:
        OddTotal = OddTotal + num
    print("Sum of Odd Numbers in provided list : ",OddTotal)

def main():
    #print("Inside Main")

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    input_list = []
    for i in range(1,N+1):
        num = int(input())
        input_list.append(num)

    print("List of entered numbers : ",input_list)

    Even_T1 = threading.Thread(target=AddEven,args=(input_list,))      #Creation of Thread
    Even_T1.start()                                     #To start the Thread
    Even_T1.join()

    Odd_T2 = threading.Thread(target=AddOdd,args=(input_list,))        #Creation of Thread
    Odd_T2.start()                                      #To start the Thread
    Odd_T2.join()

if __name__ =="__main__":
    main()
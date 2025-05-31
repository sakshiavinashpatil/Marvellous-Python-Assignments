import threading

def EvenFactor(num):
    #print("Inside EvenFactor")
    EvenTotal = 0
    for i in range(1,num+1):
        if num % i == 0 and i % 2 == 0:
            EvenTotal = EvenTotal + i
    print("Sum of Even Factors : ",EvenTotal)

def OddFactor(num):
    #print("Inside OddFactor")
    OddTotal = 0
    for i in range(1,num+1):
        if num % i == 0 and i % 2 != 0:
            OddTotal = OddTotal + i
    print("Sum of Odd Factors : ",OddTotal)

def main():
    #print("Inside Main")
    try:
        print("Enter an Integer : ")
        no = int(input())
    except ValueError:
        print("Invalid input, please enter an integer.")
        return


    Even_T1 = threading.Thread(target=EvenFactor, args=(no,))       #Creation of Thread
    Even_T1.start()                                                 #To start the Thread
    Even_T1.join()

    Odd_T2 = threading.Thread(target=OddFactor, args=(no,))        #Creation of Thread
    Odd_T2.start()                                                  #To start the Thread
    Odd_T2.join()

    print("Exit from main")

if __name__ =="__main__":
    main()
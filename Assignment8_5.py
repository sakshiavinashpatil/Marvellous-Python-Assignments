import threading

def Asc():
    #print("Inside Asc")
    print("Printing 1 to 50 : ")
    for i in range(1,51):
        print(i,end=' ')
    print()

def Desc():
    #print("Inside Desc")
    print("Printing 50 to 1 : ")
    for i in range(50,0,-1):
        print(i,end=' ')
    print()

def main():
    #print("Inside Main")

    T1 = threading.Thread(target=Asc)      #Creation of Thread
    T1.start()                                     #To start the Thread
    T1.join()

    T2 = threading.Thread(target=Desc)        #Creation of Thread
    T2.start()                                      #To start the Thread
    T2.join()

if __name__ =="__main__":
    main()
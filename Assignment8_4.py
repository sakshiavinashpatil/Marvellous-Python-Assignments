import threading

def Small(input_string):
    #print("Inside Small")

    count = 0
    for i in input_string:
        if i.islower():
            count =  count + 1
    print("Count of small letters : ",count)

def Capital(input_string):
    #print("Inside Capital")

    count = 0
    for i in input_string:
        if i.isupper():
            count =  count + 1
    print("Count of Capital letters : ",count)

def Digits(input_string):
    #print("Inside Digits")
    
    count = 0
    for i in input_string:
        if i.isdigit():
            count =  count + 1
    print("Count of Digits : ",count)

def main():
    #print("Inside Main")

    print("Enter a string : ")
    input_string = input()

    print("String provided : ",input_string)

    Small_T1 = threading.Thread(target=Small,args=(input_string,))      #Creation of Thread
    Small_T1.start()                                     #To start the Thread
    print("Thread 1 Name : ",Small_T1.name)
    print("Thread 1 ID : ",Small_T1.ident)
    Small_T1.join()

    Capital_T2 = threading.Thread(target=Capital,args=(input_string,))        #Creation of Thread
    Capital_T2.start()                                      #To start the Thread
    print("Thread 2 Name : ",Capital_T2.name)
    print("Thread 2 ID : ",Capital_T2.ident)
    Capital_T2.join()

    Digit_T3 = threading.Thread(target=Digits,args=(input_string,))      #Creation of Thread
    Digit_T3.start()                                     #To start the Thread
    print("Thread 3 Name : ",Digit_T3.name)
    print("Thread 3 ID : ",Digit_T3.ident)
    Digit_T3.join()

if __name__ =="__main__":
    main()
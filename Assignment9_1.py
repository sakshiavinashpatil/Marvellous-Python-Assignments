import threading
import time

def numbers():
    #print("Inside DisplayEven")
    for i in range(1,6):
        print(i)
        time.sleep(1)

def main():
    #print("Inside Main")
    T1 = threading.Thread(target=numbers)   
    T2 = threading.Thread(target=numbers)    
    T3 = threading.Thread(target=numbers)    

    T1.start()                                   
    T2.start()                                   
    T3.start()                                   

    T1.join()
    T2.join()
    T3.join()

if __name__ =="__main__":
    main()
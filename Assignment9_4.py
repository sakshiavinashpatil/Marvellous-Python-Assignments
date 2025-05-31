import time
import threading
import multiprocessing

def sum():
    total = 0
    for i in range(1,10_000_001):
        total = total + i
    return total

def thread_sum():
    sum()

def process_sum():
    sum()

def main():
    #print("Inside Main")

    #NORMAL
    start = time.time()
    sum()
    end = time.time()
    print(f"Normal execution time : {end-start}")

    #THREADING
    T = threading.Thread(target=thread_sum)  
    start = time.time()   
    T.start()                                                                    
    T.join()
    end = time.time()
    print(f"Thread execution time : {end-start}")

    #MULTIPROCESSING

    P =  multiprocessing.Process(target=process_sum)
    start = time.time()   
    P.start()                                                                    
    P.join()
    end = time.time()
    print(f"Process execution time : {end-start}")

if __name__ =="__main__":
    main()
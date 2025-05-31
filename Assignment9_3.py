import multiprocessing
import math

def factorial(num):
    return math.factorial(num)

def main():
    #print("Inside Main")

    no = [1,2,3,4,5,6,7,8,9,10]

    with multiprocessing.Pool() as P:
        result = P.map(factorial,no)

    print("Factorials of provided numbers : " , result)

if __name__ =="__main__":
    main()
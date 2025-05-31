import multiprocessing

def square(num):
    square = num * num
    return square

def main():
    #print("Inside Main")

    no = [1,2,3,4,5,6,7,8,9,10]

    with multiprocessing.Pool() as P:
        result = P.map(square,no)

    print("Squares of provided numbers : " , result)

if __name__ =="__main__":
    main()
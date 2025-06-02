from functools import reduce

def ChkPrime(no):
    if no <= 1:
        return False
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

def Mul(no):
    return no * 2

def Max(no1, no2):
    return no1 if no1 > no2 else no2

def main(): 

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    input_list = []
    for i in range(1,N+1):
        num = int(input())
        input_list.append(num)

    print("Input List : ",input_list)

    Fdata = list(filter(ChkPrime, input_list))
    print("List after Filter : ",Fdata)

    Mdata = list(map(Mul, Fdata))
    print("List after Map : ", Mdata)

    if Mdata:
        Rdata = reduce(Max, Mdata)  
    else:
        Rdata = None
    print("Output of Reduce : ",Rdata)

if __name__ =="__main__":
    main()
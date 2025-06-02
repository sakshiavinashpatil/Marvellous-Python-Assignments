from functools import reduce

def main(): 

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    input_list = []
    for i in range(1,N+1):
        num = int(input())
        input_list.append(num)

    print("Input List : ",input_list)

    Fdata = list(filter(lambda no : 70 <= no <= 90, input_list))
    print("List after Filter : ",Fdata)

    Mdata = list(map(lambda no : no + 10, Fdata))
    print("List after Map : ", Mdata)

    if Mdata:
        Rdata = reduce(lambda no1, no2 : no1 * no2, Mdata)  
    else:
        Rdata = 0
    print("Output of Reduce : ",Rdata)

if __name__ =="__main__":
    main()
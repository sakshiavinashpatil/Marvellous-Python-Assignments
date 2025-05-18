def main():

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    list = []
    for i in range(1,N+1):
        num = int(input())
        list.append(num)

    print("List of entered numbers : ",list)

    Add = 0
    for i in list:
        Add = Add + i

    print("Addition of all the numbers in the list : ",Add)

if __name__ == "__main__":
    main()
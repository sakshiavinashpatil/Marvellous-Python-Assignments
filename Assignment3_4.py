def main():

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    list_output = []
    for i in range(1,N+1):
        num = int(input())
        list_output.append(num)

    print("List of entered numbers : ",list_output)

    no = int(input("Enter a number from above list to check its frequency in the list : "))

    count = 0
    for no in list_output:
        count = count + 1

    print(f"Frequency of {no} in the list : ",count)

if __name__ == "__main__":
    main()
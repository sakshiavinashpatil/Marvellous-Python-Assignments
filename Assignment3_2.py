def main():

    print("Enter the count of numbers to be accepted : ")
    N = int(input())

    print(f"Enter {N} numbers : ")
    list = []
    for i in range(1,N+1):
        num = int(input())
        list.append(num)

    print("List of entered numbers : ",list)

    max_value = list[0]

    for i in list:
        if i > max_value:
            max_value = i

    print("Maximum value of among the numbers in the list : ",max_value)

if __name__ == "__main__":
    main()
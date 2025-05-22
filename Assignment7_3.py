def main():

    print("Enter count of numbers in List : ")
    count = int(input())

    print("Enter list:")
    list_no = []

    for i in range(count):
        no = int(input())
        list_no.append(no)
    

    print("Input Data : ",list_no)

    FData = list(filter(lambda no : no % 2 == 0 ,list_no))
    print("Even numbers : ",FData)

if __name__ == "__main__":
    main()
    
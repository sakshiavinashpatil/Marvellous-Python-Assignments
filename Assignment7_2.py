def main():

    print("Enter count of numbers in List : ")
    count = int(input())

    print("Enter list:")
    list_no = []

    for i in range(count):
        no = int(input())
        list_no.append(no)
    

    print("Input Data : ",list_no)

    MData = list(map(lambda no : 2 * no ,list_no))
    print("Doubled List : ",MData)

if __name__ == "__main__":
    main()
    
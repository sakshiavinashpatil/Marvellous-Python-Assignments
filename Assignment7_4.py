import functools 

def main():

    print("Enter count of numbers in List : ")
    count = int(input())

    print("Enter list:")
    list_no = []

    for i in range(count):
        no = int(input())
        list_no.append(no)
    

    print("Input Data : ",list_no)

    RData = functools.reduce(lambda mul, no: mul * no, list_no)
    print("Even numbers : ",RData)

if __name__ == "__main__":
    main()
    
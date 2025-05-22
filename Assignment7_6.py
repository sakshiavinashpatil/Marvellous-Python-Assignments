def ChkPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():

    print("Enter count of numbers in List : ")
    count = int(input())

    print("Enter list:")
    list_no = []

    for i in range(count):
        no = int(input())
        list_no.append(no)
    
    print("Input Data : ",list_no)

    FData = list(filter(ChkPrime, list_no))
    print("Prime numbers : ",FData)

if __name__ == "__main__":
    main()
    
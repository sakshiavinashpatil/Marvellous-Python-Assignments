def ChckPrime(no)  :
    if no < 2:
        return False
    else:
        for i in range(2,(no+1)):
            if no % i == 0:
                return False
            else:
                return True

def main():

    print("Enter a number : ")
    num = int(input())

    result = ChckPrime(num)

    if result:
        print(f"{num} IS PRIME")
    else:
        print(f"{num} NOT PRIME")
    

if __name__ == "__main__":
    main()
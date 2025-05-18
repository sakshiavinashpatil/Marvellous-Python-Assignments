def CheckPrime(num):

    if num <=1:
        return False
    
    for i in range(2,num):
        if num % i == 0 :
            return False
    else:
        return True

def main():
    print("Enter a number :")
    no = int(input())

    Result = CheckPrime(no)

    print(f"{no} is a Prime Number" if Result == True else f"{no} is NOT a Prime Number")

if __name__ == "__main__":
    main()

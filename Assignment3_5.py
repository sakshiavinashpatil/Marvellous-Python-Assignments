def ChkPrime(num):
    
    if num <=1:
        return False
    
    for i in range(2,num):
        if num % i == 0 :
            return False
    else:
        return True

def listPrime(numbers):
    prime_sum = 0
    for num in numbers:
        if ChkPrime(num):
            prime_sum += num
    return prime_sum

def main():
    N = int(input("Enter the count of numbers: "))
    numbers = []

    for i in range(N):
        num = int(input())
        numbers.append(num)

    result = listPrime(numbers)
    print("Sum of all prime numbers:", result)

if __name__ == "__main__":
    main()
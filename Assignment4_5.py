from functools import reduce

def ChkPrime(num):
    if num <=1:
        return False
    
    for i in range(2,num):
        if num % i == 0 :
            return False
    else:
        return True

def main():
    input_list = [2, 70, 11, 10, 17, 23, 31, 77]

    filtered = list(filter(ChkPrime, input_list))
    print("Filtered =", filtered)

    mapped = list(map(lambda no : no * 2, filtered))
    print("Mapped =", mapped)

    maximum = reduce(lambda no1, no2: no1 if no1 > no2 else no2, mapped)
    print("Reduced =", maximum)

if __name__ == "__main__":
    main()
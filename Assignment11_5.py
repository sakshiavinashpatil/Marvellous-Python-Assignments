def Count(n):
    if n == 0:
        return 1  
    if n < 10:
        return 0
    if n % 10 == 0:
        return 1 + Count(n // 10)
    else:
        return Count(n // 10)

def main():
    num = int(input("Enter a number : "))

    if num < 0:
        num = abs(num)  

    result = Count(num)
    print("Count of zeros :", result)

if __name__ == "__main__":
    main()
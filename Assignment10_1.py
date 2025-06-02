def main():
    power = lambda no : no ** 2

    print("Enter a number : ")
    num = int(input())
    
    result = power(num)
    print(f"Power of two is : ",result)

if __name__ =="__main__":
    main()
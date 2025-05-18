def Factorial(num):
    if num >= 0:
        output = 1
        for i in range(1,num+1):
            output = output * i
        return output
    else:
        print("Number entered is invalid")
        return None

def main():
    print("Enter a number to calculate its factorial :")
    no = int(input())

    Result = Factorial(no)

    if Result is not None:
        print(f"factorial of {no} is : ",Result)

if __name__ == "__main__":
    main()
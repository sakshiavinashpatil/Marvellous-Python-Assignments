Multiplication = lambda no1,no2 : no1 * no2

def main():
    print("Enter two numbers : ")
    no1 = int(input())
    no2 = int(input())
    
    result = Multiplication(no1,no2)
    print("Output:", result)

if __name__ == "__main__":
    main()
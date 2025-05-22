def main():

    print("Enter a number : ")
    no = int(input())

    fact = 1
    i = 1

    while i <= (no):
        fact = fact * i
        i = i + 1
        

    print(f"Factorial of {no} is : ", fact)

    
if __name__ == "__main__":
    main()
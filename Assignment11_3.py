def Sum(num):
    if num == 0:
        return 0
    return (num % 10) + Sum(num // 10)

def main():
    no = int(input("Enter a number : "))
    
    if no < 0:
        print("Invalid number.")
    else:
        result = Sum(no)
        print("Sum_of_digits :", result)

if __name__ == "__main__":
    main()
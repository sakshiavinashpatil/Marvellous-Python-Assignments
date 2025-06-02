def Fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * Fact(num - 1)

def main():
    print("Enter a number : ")
    no = int(input())
    
    if no < 0:
        print("Invalid number.")
    else:
        result = Fact(no)
        print(f"Factorial({no}) :", result)

if __name__ == "__main__":
    main()
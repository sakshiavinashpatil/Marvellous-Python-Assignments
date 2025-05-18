def main():
    print("Enter a number to print pattern :")
    no = int(input())   #12345

    no1 = str(abs(no))  #12345

    Add = 0
    for i in no1:
        Add = Add + int(i)

    print(f"The addition of digits in {no} number is : ",Add)

if __name__ == "__main__":
    main()

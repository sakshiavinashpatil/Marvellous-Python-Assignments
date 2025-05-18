def main():
    print("Enter a number to print pattern :")
    no = int(input())

    count = len(str(abs(no)))

    print(f"The number of digits in {no} is : ",count)

if __name__ == "__main__":
    main()

def main():
    print("Enter a number to print pattern :")
    no = int(input())

    for i in range(no):
        for j in range(no-i):
            print("*",end="")
        print("")      

if __name__ == "__main__":
    main()

def main():
    print("Enter a number to print pattern :")
    no = int(input())

    print("The Expected pattern is : ")
    for i in range(no):
        for j in range(1,(i+2)):
            print(j,end="")
            j = j + 1
        print()

if __name__ == "__main__":
    main()

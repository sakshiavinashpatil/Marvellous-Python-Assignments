def main():
    print("Enter number to print Grid of Stars: ")
    no = int(input())

    for j in range(no):
        for i in range(no):
            print("*",end="")
        print("")

if __name__ == "__main__":
    main()
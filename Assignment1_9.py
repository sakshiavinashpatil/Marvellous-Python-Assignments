def main():
    print("How many first Even numbers to be printed?")
    num = int(input())

    print (f"The First {num} Even numbers are :")
    for i in range(0,2*num,2):
        print (i)

if __name__ == "__main__":
    main()
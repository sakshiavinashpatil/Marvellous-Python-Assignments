def main():
    print("Enter number of * to be printed:")
    count = int(input())

    i = 0
    while i < count:
        print("*",end=' ')
        i = i + 1

if __name__ == "__main__":
    main()

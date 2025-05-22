def main():

    print("Enter 5 numbers : ")
    no1 = int(input())
    no2 = int(input())
    no3 = int(input())
    no4 = int(input())
    no5 = int(input())

    max = no1

    if no2 > max:
        max = no2
    if no3 > max:
        max = no3
    if no4 > max:
        max = no5
    if no5 > max:
        max = no5

    print("Maximum number : ", max)

if __name__ == "__main__":
    main()
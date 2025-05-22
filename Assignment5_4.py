def main():

    print("Enter 3 numbers: ")
    print("1st number:")
    no1 = int(input())

    print("2nd number:")
    no2 = int(input())

    print("3rd number:")
    no3 = int(input())
    
    if no1 > no2:
        if no1 > no3:
            print(f"{no1} is greatest.")
        else:
            print(f"{no3} is the greatest.")
    else:
        if no2 > no3:
            print(f"{no2} is the greatest.")
        else:
            print(f"{no3} is the greatest.")   

if __name__ == "__main__":
    main()
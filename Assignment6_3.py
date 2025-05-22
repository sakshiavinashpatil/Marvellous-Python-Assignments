def main():

    print("Enter a number : ")
    no = int(input())

    i = 1
    while i < 11:
        table = no * i
        print(f"{no} * {i} = ",table)
        i = i + 1
    
if __name__ == "__main__":
    main()
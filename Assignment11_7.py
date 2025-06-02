def Display(col):
    if col == 0:
        return
    print("*", end=" ")
    Display(col - 1)

def print_pattern(row):
    if row == 0:
        return
    print_pattern(row - 1)
    Display(row)
    
    print()  

def main():
    no = int(input("Enter number of rows : "))
    print_pattern(no)

if __name__ == "__main__":
    main()
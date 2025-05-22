def main():

    print("Enter a number : ")
    no = int(input())

    Square = lambda no : (no * no)
    Cube = lambda no : (no * no * no)

    ret1 = Square(no)
    ret2 = Cube(no)

    print("Square : ", ret1)
    print("Cube : ", ret2)

if __name__ == "__main__":
    main()
    
import Arithmetic

def main():
    print("Enter First number : ")
    num1 = int(input())

    print("Enter Second number : ")
    num2 = int(input())

    Sum = Arithmetic.Sum(num1, num2)
    Difference = Arithmetic.Difference(num1, num2)
    Product = Arithmetic.Product(num1, num2)
    Division = Arithmetic.Division(num1, num2)

    print("Sum = ",Sum)
    print("Difference = ",Difference)
    print("Product = ",Product)
    print("Division = ",Division)


if __name__ == "__main__":
    main()
import Arithmetic

def main():

    print("Enter 2 numbers for Addition:")
    print("Enter 1st Number:")
    no1 = int(input())

    print("Enter 2nd Number:")
    no2 = int(input())

    Result = Arithmetic.Add(no1,no2)
    print(f"Addition of {no1} and {no2} : ",Result)

    print("------------------------------------------------------")

    print("Enter 2 numbers for Substraction:")
    print("Enter 1st Number:")
    no1 = int(input())

    print("Enter 2nd Number:")
    no2 = int(input())

    Result = Arithmetic.Sub(no1,no2)
    print(f"Substraction of {no1} and {no2} : ",Result)

    print("------------------------------------------------------")

    print("Enter 2 numbers for Multiplication:")
    print("Enter 1st Number:")
    no1 = int(input())

    print("Enter 2nd Number:")
    no2 = int(input())

    Result = Arithmetic.Mul(no1,no2)
    print(f"Multiplication of {no1} and {no2} : ",Result)

    print("------------------------------------------------------")

    print("Enter 2 numbers for Division:")
    print("Enter 1st Number:")
    no1 = int(input())

    print("Enter 2nd Number:")
    no2 = int(input())

    Result = Arithmetic.Div(no1,no2)
    print(f"Division of {no1} and {no2} : ",Result)
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
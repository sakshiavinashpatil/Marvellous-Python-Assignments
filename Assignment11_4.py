def Power(B, E):
    if E == 0:
        return 1
    return B * Power(B, E - 1)

def main():

    B = int(input("Enter base number: "))
    E = int(input("Enter exponent number : "))
    
    result = Power(B, E)
    print(f"{B} raised to the power {E} is : ",result)

if __name__ == "__main__":
    main()
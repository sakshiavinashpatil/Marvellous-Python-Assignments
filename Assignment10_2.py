def main():
    mul = lambda A, B : A * B

    print("Enter two numbers : ")
    no1 = int(input())
    no2 = int(input())

    result = mul(no1, no2)
    print(f"Output : ",result)

if __name__ =="__main__":
    main()
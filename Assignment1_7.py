def Output(value1):
    output = value1 % 5
    return output 

def main():
    print("Enter a number:")
    num =  int(input())

    result = Output(num)

    print("True" if result == 0 else "False")

if __name__ == "__main__":
    main()

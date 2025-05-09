def ChkNum(value):
    output = value % 2
    return output

def main():
    print("Enter a number:")
    num = int(input())
    
    result = ChkNum(num) 
    print ("Even Number" if result==0 else "Odd Number")

if __name__ == "__main__":
    main()
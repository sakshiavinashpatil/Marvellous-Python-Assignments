def main():
    print("Enter a number :")
    no = int(input())

    Add = 0
    for i in range(1,(no)):
        #output = no % i
        #print(output)
        
        if no % i == 0:    
            Add = Add + i
    
    print(f"Addition of Factors of {no} is :", Add)

if __name__ == "__main__":
    main()
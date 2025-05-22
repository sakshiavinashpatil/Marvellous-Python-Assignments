def main():

    print("Enter your age: ")
    age = int(input())
    
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("NOT eligible to vote.")

if __name__ == "__main__":
    main()
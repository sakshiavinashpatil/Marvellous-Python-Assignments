def main():
    print("Enter a name")
    Name = str(input())

    print(f"The length of {Name} is: ")
    i=0
    while i < len(Name):
        i = i+1
    print(i)

if __name__ == "__main__":
    main()
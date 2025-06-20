def main():
    with open("numbers.txt", "w") as f:
        for i in range(10):
            num = input("Enter a number: ")
            f.write(num + "\n")

if __name__ == "__main__":
    main()
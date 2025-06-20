def main():
    src = input("Enter source file: ")
    with open(src, "r") as f1, open("destination.txt", "w") as f2:
        f2.write(f1.read())
    print("Copied to destination.txt")

if __name__ == "__main__":
    main()
def main():
    fname = input("Enter file name: ")
    with open(fname, "r") as f:
        for line in f:
            if len(line.split()) > 5:
                print(line.strip())

if __name__ == "__main__":
    main()
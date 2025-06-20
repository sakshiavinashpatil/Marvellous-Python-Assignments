def main():
    fname = input("Enter file name: ")
    with open(fname, "r") as f1, open("cleaned.txt", "w") as f2:
        for line in f1:
            if line.strip():
                f2.write(line)
    print("Blank lines removed.")

if __name__ == "__main__":
    main()
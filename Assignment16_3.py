def main():
    file = input("Enter file name: ")
    with open(file, "r") as f:
        text = f.readlines()
        lines = len(text)
        words = sum(len(line.split()) for line in text)
        chars = sum(len(line) for line in text)
        print("Lines:", lines)
        print("Words:", words)
        print("Characters:", chars)

if __name__ == "__main__":
    main()
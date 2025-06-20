def main():
    with open("marks.txt", "r") as f:
        for line in f:
            name, marks = line.split()
            if int(marks) > 75:
                print(name)

if __name__ == "__main__":
    main()
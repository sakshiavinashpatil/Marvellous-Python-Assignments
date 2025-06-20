def main():

    with open("student.txt", "w") as f:

        for i in range(1,6):
            name = input(f"Enter student {i} name: ")
            f.write(name + "\n")

if __name__ == "__main__":
    main()
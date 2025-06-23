def Display_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} not found.")

def main():
    filename = input("Enter file name: ")
    Display_file_contents(filename)

if __name__ == "__main__":
    main()

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            print("File contents:\n", file.read())
    except FileNotFoundError:
        print("File not found.")

def main():
    filename = input("Enter the file name: ")
    display_file_contents(filename)

if __name__ == "__main__":
    main()
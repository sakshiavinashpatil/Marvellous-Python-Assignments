import os

def check_file_exists(filename):
    if os.path.exists(filename):
        print(f"{filename} exists.")
    else:
        print(f"{filename} does not exist.")

def main():
    filename = input("Enter the file name: ")
    check_file_exists(filename)

if __name__ == "__main__":
    main()
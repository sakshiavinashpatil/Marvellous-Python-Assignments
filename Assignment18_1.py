import os

def Chk_file_exists(filename):
    return os.path.isfile(filename)

def main():
    filename = input("Enter file name: ")
    if Chk_file_exists(filename):
        print(f"{filename} exists.")
    else:
        print(f"{filename} does not exist.")

if __name__ == "__main__":
    main()
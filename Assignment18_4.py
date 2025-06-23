import sys

def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            if f1.read() == f2.read():
                print("Success: Files are same.")
            else:
                print("Failure: Files are not same.")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py file1.txt file2.txt")
    else:
        compare_files(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

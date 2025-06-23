import sys

def copy_to_demo(source_file):
    try:
        with open(source_file, 'r') as src, open("Demo.txt", 'w') as dest:
            dest.write(src.read())
        print(f"Contents of {source_file} copied to Demo.txt.")
    except FileNotFoundError:
        print(f"{source_file} not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py source_file.txt")
    else:
        copy_to_demo(sys.argv[1])

if __name__ == "__main__":
    main()

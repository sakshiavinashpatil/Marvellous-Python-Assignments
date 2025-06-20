import sys

def copy_file_contents(src_filename, dst_filename="Demo.txt"):
    try:
        with open(src_filename, 'r') as src, open(dst_filename, 'w') as dst:
            dst.write(src.read())
        print(f"Contents of {src_filename} copied to {dst_filename}.")
    except FileNotFoundError:
        print("Source file not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <source_file>")
    else:
        src_filename = sys.argv[1]
        copy_file_contents(src_filename)

if __name__ == "__main__":
    main()
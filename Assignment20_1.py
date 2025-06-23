import hashlib
import os
import sys

def generate_checksum(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryChecksum.py <directory>")
        return

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Invalid directory")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            checksum = generate_checksum(filepath)
            print(f"{filename}: {checksum}")

if __name__ == "__main__":
    main()
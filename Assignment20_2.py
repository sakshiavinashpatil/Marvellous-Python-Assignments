import hashlib
import os
import sys

def get_checksum_map(directory):
    checksum_map = {}
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            checksum = hashlib.md5(open(path, 'rb').read()).hexdigest()
            checksum_map.setdefault(checksum, []).append(file)
    return checksum_map

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicate.py <directory>")
        return

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Invalid directory")
        return

    checksum_map = get_checksum_map(directory)
    with open("Log.txt", "w") as log:
        for files in checksum_map.values():
            if len(files) > 1:
                log.write("Duplicate group: " + ", ".join(files) + "\n")
    print("Log.txt created.")

if __name__ == "__main__":
    main()
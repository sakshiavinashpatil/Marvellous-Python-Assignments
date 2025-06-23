import hashlib
import os
import sys

def remove_duplicates(directory):
    checksum_map = {}
    deleted = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            checksum = hashlib.md5(open(path, 'rb').read()).hexdigest()
            if checksum in checksum_map:
                os.remove(path)
                deleted.append(file)
            else:
                checksum_map[checksum] = file
    return deleted

def main():
    if len(sys.argv) != 2:
        print("Usage: python DirectoryDuplicateRemoval.py <directory>")
        return

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Invalid directory")
        return

    deleted_files = remove_duplicates(directory)
    with open("Log.txt", "w") as log:
        for file in deleted_files:
            log.write(f"Deleted: {file}\n")
    print("Duplicates deleted and log file is created.")

if __name__ == "__main__":
    main()
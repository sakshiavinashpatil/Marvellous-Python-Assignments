import os
import sys

def search_files_by_extension(directory, extension):
    for file in os.listdir(directory):
        if file.endswith(extension):
            print(file)

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryFileSearch.py <directory> <extension>")
        return
    directory = sys.argv[1]
    extension = sys.argv[2]
    search_files_by_extension(directory, extension)

if __name__ == "__main__":
    main()
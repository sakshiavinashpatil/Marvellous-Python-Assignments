import os
import sys

def rename_extensions(directory, old_ext, new_ext):
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            new_name = filename.replace(old_ext, new_ext)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed: {filename} → {new_name}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python DirectoryRename.py <directory> <old_ext> <new_ext>")
        return
    directory = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    rename_extensions(directory, old_ext, new_ext)

if __name__ == "__main__":
    main()
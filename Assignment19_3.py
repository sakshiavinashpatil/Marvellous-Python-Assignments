import os
import shutil
import sys

def copy_all_files(src_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for filename in os.listdir(src_dir):
        full_path = os.path.join(src_dir, filename)
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_dir)
            print(f"Copied: {filename}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python DirectoryCopy.py <source_directory> <target_directory>")
        return
    src = sys.argv[1]
    dest = sys.argv[2]
    copy_all_files(src, dest)

if __name__ == "__main__":
    main()
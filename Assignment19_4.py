import os
import shutil
import sys

def copy_files_by_extension(src_dir, dest_dir, extension):
    os.makedirs(dest_dir, exist_ok=True)
    for filename in os.listdir(src_dir):
        if filename.endswith(extension):
            shutil.copy(os.path.join(src_dir, filename), dest_dir)
            print(f"Copied: {filename}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python DirectoryCopyExt.py <source_directory> <target_directory> <extension>")
        return
    src = sys.argv[1]
    dest = sys.argv[2]
    ext = sys.argv[3]
    copy_files_by_extension(src, dest, ext)

if __name__ == "__main__":
    main()
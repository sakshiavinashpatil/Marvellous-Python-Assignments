def count_string_frequency(filename, search_str):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.count(search_str)
            print(f"The string '{search_str}' occurs {count} time(s) in {filename}.")
    except FileNotFoundError:
        print("File not found.")

def main():
    filename = input("Enter the file name: ")
    search_str = input("Enter the string to search: ")
    count_string_frequency(filename, search_str)

if __name__ == "__main__":
    main()
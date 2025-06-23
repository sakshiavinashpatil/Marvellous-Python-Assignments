def count_string_frequency(filename, input_string):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            count = content.count(input_string)
            print(f"The string '{input_string}' occurred {count} times in {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found.")

def main():
    filename = input("Enter file name: ")
    input_string = input("Enter string to search: ")
    count_string_frequency(filename, input_string)

if __name__ == "__main__":
    main()

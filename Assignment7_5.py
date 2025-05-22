def main():

    print("Enter a string : ")
    palindrome = input()

    if palindrome == palindrome[::-1]:
        print(f"{palindrome} is a palindrome.")
    else:
        print(f"{palindrome} is NOT a palindrome.")

if __name__ == "__main__":
    main()
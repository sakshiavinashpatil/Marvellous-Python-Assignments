def main():

    print("Enter a single alphabet: ")
    alphabet = input()
    
    if len(alphabet) == 1:
        if alphabet in 'aeiou':
            print(f"{alphabet} is a vowel.")
        else:
            print(f"{alphabet} is a consonant.")
    else:
        print("Please enter a valid aplhabet.")

if __name__ == "__main__":
    main()
def main():
    print("Enter an Integer:")
    num = int(input())
    print("Positive Integer" if num > 0 else "Negative Integer" if num < 0 else "Zero")

if __name__ == "__main__":
    main()
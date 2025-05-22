def main():

    print("Enter a number: ")
    no = int(input())

    print(f"{no} is an even number." if no % 2 == 0 else f"{no} is an odd number")
     
if __name__ == "__main__":
    main()
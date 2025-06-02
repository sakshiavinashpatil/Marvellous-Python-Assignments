def Display(i, no):
    if i > no:
        return
    print(i, end=' ')
    Display(i + 1 , no)

def main():
    print("Enter a number : ")
    num = int(input())

    Display(1, num)

if __name__ == "__main__":
    main()
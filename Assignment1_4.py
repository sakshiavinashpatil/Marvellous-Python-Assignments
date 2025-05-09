def Repeat():
    Value =  "Marvellous"
    return Value

def main():
    i=0
    while (i < 5):
        output = Repeat()
        print(output)
        i = i + 1

if __name__ == "__main__":
    main()
def main():

    print("Enter Length : ")
    length = int(input())

    print("Enter Width : ")
    width = int(input())

    area = length * width
    perimeter = 2 * (length + width)

    print("Area : ", area )
    print("Perimeter : " ,perimeter)
     
if __name__ == "__main__":
    main()
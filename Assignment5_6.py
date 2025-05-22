def main():

    print("Enter Temperature in Celcius : ")
    temp_C = int(input())

    temp_F1 = (temp_C * (9/5)) + 32
    temp_F = str(temp_F1) + '\u00B0F'

    print("Temperature in Fahrenheit : ", temp_F )
     
if __name__ == "__main__":
    main()
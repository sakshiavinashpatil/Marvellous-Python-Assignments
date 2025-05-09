def Add(value1,value2):
    sum = value1 + value2
    return sum

print("Enter 2 numbers:")
num1 = int(input())
num2 = int(input())

result = Add(num1,num2)
print(f"Addition of {num1} and {num2} is:",result)
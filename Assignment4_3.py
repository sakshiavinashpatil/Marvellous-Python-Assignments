from functools import reduce

def main():
    input_list = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    filtered = list(filter(lambda no1 : 70 <= no1 <= 90, input_list))
    print("Filtered =", filtered)
    
    mapped = list(map(lambda no1 : no1 + 10, filtered))
    print("Mapped =", mapped)
    
    reduced = reduce(lambda no1, no2 : no1 * no2, mapped)
    print("Reduced =", reduced)

if __name__ == "__main__":
    main()
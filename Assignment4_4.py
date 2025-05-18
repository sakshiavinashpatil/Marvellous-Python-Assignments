from functools import reduce

def main():
    input_list = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    filtered = list(filter(lambda no: no % 2 == 0, input_list))
    print("Filtered =", filtered)

    mapped = list(map(lambda no: no ** 2, filtered))
    print("Mapped =", mapped)

    total = reduce(lambda no1, no2: no1 + no2, mapped)
    print("Reduced =", total)

if __name__ == "__main__":
    main()
class Book:
    def __init__(self, price):
        self.__price = price  # This is private attribute

    def set_price(self, new_price):
        self.__price = new_price

    def get_price(self):
        return self.__price

b = Book(400)
print("Old Price:", b.get_price())
b.set_price(500)
print("New Price:", b.get_price())
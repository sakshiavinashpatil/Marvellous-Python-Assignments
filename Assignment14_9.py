class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

p1 = Product("Bedsheet", 1000)
p2 = Product("Pillow", 500)

if p1 == p2:
    print("Both products have equal price.")
else:
    print("Prices are different.")
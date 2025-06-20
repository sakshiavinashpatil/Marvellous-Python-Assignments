class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        print(f"Factors of {self.Value} are:", end=" ")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total = total + i
        return total

obj1 = Numbers(5)
print("Is 5 Prime?:", obj1.ChkPrime())
print("Is 5 Perfect?:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors of 5:", obj1.SumFactors())

print()

obj2 = Numbers(2)
print("Is 2 Prime?:", obj2.ChkPrime())
print("Is 2 Perfect?:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors of 2:", obj2.SumFactors())
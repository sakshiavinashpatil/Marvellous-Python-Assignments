class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Value(self):
        self.radius = float(input("Enter radius : "))

    def CircleArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CircleCicumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius : ",self.radius)
        print("Area : ",self.area)
        print("Circumference : ", self.circumference)

def main():
    obj1 = Circle()
    obj1.Value()
    obj1.CircleArea()
    obj1.CircleCicumference()
    obj1.Display()

if __name__ =="__main__":
    main()
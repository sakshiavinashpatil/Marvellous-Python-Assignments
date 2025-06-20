class Student:
    school_name = "Little Soul's School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")

s = Student("Sakshi", 28)
s.display()

Student.school_name = "S.B.O.A Public School"   #Change 
s.display()
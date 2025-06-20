class Employee:
    def __init__(self, name, department, salary):
        self.name = name                # public
        self._department = department   # protected
        self.__salary = salary          # private

    def display(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

emp = Employee("Sakshi", "CSE", 100000)
emp.display()

# Access public
print(emp.name)

# Access protected 
print(emp._department)

# Access private ----- > using name mangling
print(emp._Employee__salary)
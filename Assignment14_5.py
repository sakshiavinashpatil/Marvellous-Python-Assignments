class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

acc = BankAccount("12345678", "Sakshi", 1000)
acc.display()
acc.deposit(1500)
acc.withdraw(200)
acc.display()
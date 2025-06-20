class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self, amount):
        self.Amount = self.Amount + amount

    def Withdraw(self, amount):
        if amount <= self.Amount:
            self.Amount = self.Amount - amount
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

    def Display(self):
        print(f"Name: {self.Name}, Amount: {self.Amount}")

acc1 = BankAccount("Sakshi", 2000)
acc1.Deposit(500)            # Total: 1500
acc1.Withdraw(200)           # Total: 1300
print("Interest for acc1:", acc1.CalculateInterest())  
acc1.Display()

print()

acc2 = BankAccount("Geetanjali", 1000)
acc2.Deposit(1000)           
acc2.Withdraw(500)           
print("Interest for acc2:", acc2.CalculateInterest())  
acc2.Display()
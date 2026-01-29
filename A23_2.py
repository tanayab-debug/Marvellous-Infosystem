class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print(f"Holders name is {self.Name} and balance is {self.Amount}")

    def Deposit(self):
        self.Amt = int(input("Enter the amount to deposit: "))
        self.Amount += self.Amt
        print("available balance: ", self.Amount)

    def Withdraw(self):
        self.Wtdr = int(input("Enter the amount to withdraw: "))
        if(self.Wtdr <= self.Amount):
            self.Amount -= self.Wtdr
            print("available balance: ", self.Amount)
        else:
            print("Insufficient Balance")

    def Interest(self):
        self.interest = (self.Amount * BankAccount.ROI)/100
        print("Interest is: ", self.interest)

obj = BankAccount("Tanaya", 10000)
obj.Deposit()
obj.Withdraw()
obj.Interest()
obj.Display()

obj1 = BankAccount("Madhu", 500)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.Interest()
obj1.Display()
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def login(self):
        print(f"Welcome, {self.name}! You are logged in.")
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. Your current balance is ${self.balance}.")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. Your current balance is ${self.balance}.")
        else:
            print("Insufficient funds. Withdrawal failed.")
name = input("Enter your name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)
account.login()
account.deposit(100)
account.withdraw(50)
account.withdraw(80)

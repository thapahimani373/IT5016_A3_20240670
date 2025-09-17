class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private variable – encapsulation hides this to protect it.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Only add money through this safe method.
            print(f"Deposited {amount}. Balance: {self.__balance}")
        else:
            print("Deposit must be positive!")

    def get_balance(self):  # Safe way to see balance.
        return self.__balance

# Analysis: Encapsulation keeps the balance safe by hiding it. This makes code maintainable because I can change how balance is stored without affecting other parts. I think this is cool because it’s like locking a box!
account = BankAccount(100)
account.deposit(50)
print("Current balance:", account.get_balance())

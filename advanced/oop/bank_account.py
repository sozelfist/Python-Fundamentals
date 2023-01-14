class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Deposited {amount}, new balance is {self._balance}")

    def withdraw(self, amount: float):
        if self._balance - amount >= 0:
            self._balance -= amount
            print(f"Withdrawn {amount}, new balance is {self._balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Your balance is {self._balance}")


if __name__ == '__main__':
    account = BankAccount(1000)
    account.check_balance()  # "Your balance is 1000"
    account.deposit(500)  # "Deposited 500, new balance is 1500"
    account.withdraw(1000)  # "Withdrawn 1000, new balance is 500"
    account.withdraw(1000)  # "Insufficient funds."

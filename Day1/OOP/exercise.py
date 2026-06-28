from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def display_balance(self):
        print(f"Current Balance: Rs. {self.__balance}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.set_balance(self.get_balance() + amount)
        print(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.get_balance():
            print("Insufficient balance.")
            return

        self.set_balance(self.get_balance() - amount)
        print(f"Withdrawn: Rs. {amount}")


class CurrentAccount(BankAccount):

    OVERDRAFT_LIMIT = 5000

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        self.set_balance(self.get_balance() + amount)
        print(f"Deposited: Rs. {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > self.get_balance() + self.OVERDRAFT_LIMIT:
            print("Overdraft limit exceeded.")
            return

        self.set_balance(self.get_balance() - amount)
        print(f"Withdrawn: Rs. {amount}")


def perform_transaction(account):

    print(f"\n----- {account.account_holder}'s Account -----")

    account.display_balance()
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(7000)
    account.deposit(-100)
    account.withdraw(-50)
    account.display_balance()


savings = SavingsAccount("Suman", 1000)
current = CurrentAccount("Ram", 1000)

perform_transaction(savings)
perform_transaction(current)


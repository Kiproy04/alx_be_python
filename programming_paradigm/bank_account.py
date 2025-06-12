class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance
       

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return self.__account_balance
        else:
            raise ValueError("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance < amount:
                print("Insufficient funds")
            else:
                self.__account_balance -= amount
                return self.__account_balance
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

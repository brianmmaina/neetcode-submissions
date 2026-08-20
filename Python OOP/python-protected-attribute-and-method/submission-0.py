class Account:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    
    def display_balance(self) -> None:
        print(f"Balance: ${self.amount}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()

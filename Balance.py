class Balance:

    def __init__(self):
        self.balance =  0

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        self.balance -= balance

    def show_balance(self, balance):
        print(balance)

from Account import *
from Person import *

import time

myAccount = Account('Bob Thorton', 'Savings', 25000)

print(myAccount.account_balance())

myAccount.deposit(50000)

print(myAccount.account_balance())

myAccount.withdraw(20000)

print(myAccount.account_balance())

myAccount.interest_accrued_n_years(5)

p1 = Person(720)

print(p1.get_credit_score())

print(p1.change_credit_score())






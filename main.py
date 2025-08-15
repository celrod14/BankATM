from os.path import exists

from Account import *
from Person import *

import time

def getAccountType():
    accountOption = input("Create a savings or checking account?")
    if accountOption.title() == 'Savings':

        savingsAccount = Account('Bob Thorton', 'Savings', 25000)
        return savingsAccount
    elif accountOption.title() == 'Checking':
        checkingAccount = Account('Billy Joe', 'Checking', 30)
        return checkingAccount
    else:
        print('Invalid account type')
        exit()

account = getAccountType()

if account:
    print(account.account_balance())

    account.deposit(50000)

    print(account.account_balance())

    account.withdraw(20000)

    print(account.account_balance())

    account.interest_accrued_n_years(1)

    p1 = Person(720)

    print(p1.get_credit_score())

    # denied
    print(account.apply_loan(p1.creditScore))

    print(p1.change_credit_score())

    # approved
    print(account.apply_loan(p1.creditScore))
else:
    exit()








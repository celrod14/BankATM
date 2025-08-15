class Account:

    def __init__(self, accountHolder, accountType, accountBalance):
        self.accountHolder = accountHolder
        self.accountType = accountType
        self.accountBalance = accountBalance

    def deposit(self, accountBalance):
        self.accountBalance += accountBalance

    def withdraw(self, accountBalance):
        self.accountBalance -= accountBalance

    def account_holder(self):
        return self.accountHolder

    def account_type(self):
        return self.accountType

    def account_balance(self):
        return self.accountBalance

    def change_account_type(self, accountType):
        self.accountType = accountType
        return self.accountType

    # Interest = P x R x T
    def accrue_interest(self):
        if self.accountType == 'Checking':
            interest = 0.0
        elif self.accountType == 'Savings':
            interest = 0.41
        elif self.accountType == 'Credit':
            interest = 29.93
        else:
            interest = 0.0

        # return self.accountBalance - (self.accountBalance * interest / 30)

        accrued = self.accountBalance * interest * 1
        self.accountBalance += accrued
        print(f"Interest accrued: ${accrued:.2f}")
        return self.accountBalance

    '''dispolays the accrued interest over n number of years'''
    def interest_accrued_n_years(self, years):
        for i in range(0, years):
            print(self.account_balance())

            self.accrue_interest()

    def apply_loan(self, creditScore):
        if creditScore >= 730:
            loanStatus = 'Approved'
            return loanStatus
        else:
            loanStatus = 'Denined'
            return loanStatus
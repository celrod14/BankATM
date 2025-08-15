class Person:

    def __init__(self, creditScore):
        self.name = ''
        self.creditScore = creditScore

    def get_name(self):
        return self.name

    def change_name(self):
        newName = input('Please change your name')

        self.name = newName

    def get_credit_score(self):
        return self.creditScore

    def change_credit_score(self):
        if self.creditScore < 730:
            self.creditScore += 100
        return f'Credit increased to {self.creditScore}'
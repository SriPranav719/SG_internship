class BankAccount:
    balance = 0

    def deposit(self,add_amount : float):

        self.add_amount = add_amount
        self.balance = self.balance + add_amount

        return (f"amount added successfully {self.balance}")

    def withdrawn(self, withdraw : float):

        self.withdraw = withdraw

        if self.add_amount <= self.balance:
            self.balance = self.balance - self.withdraw

            return (f" amount: {self.withdraw} withdrawn successfully, remaining balance: {self.balance}")

        else:

            return "Insufficient Funds"
class LoanAccount(BankAccount):

    loan_amount = 0

    def personal_loan(self,loan : float):

        self.loan = loan

        if self.balance > 50000:

            self.loan_amount = self.loan + self.loan * self.interest_rate

            return(f"Loan amount has successfully credited, balance is :{self.balance}, loan taken {self.loan_amount} including intrest amount ")

        else:
            return ("Cannot credit loan as your account hold 'Insufficient funds !'")


class SavingsAccount(LoanAccount):

    interest_rate = 0.2

    def add_interest(self):

        self.balance = self.balance + self.balance * self.interest_rate
        return (f"intrest amount has been added, updated balance {self.balance}")



obj1 = SavingsAccount()
print(obj1.deposit(500000))

print(obj1.withdrawn(1000))

print(obj1.add_interest())

print(obj1.personal_loan(100000))
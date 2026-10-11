from BankAccount import BankAccount
import datetime

class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, accountHolder, balance, interestRate=0.02, minimumBalance=100):
        super().__init__(accountNumber, accountHolder, balance)

        self.__interestRate = interestRate
        self.__minimumBalance = minimumBalance

    def withdraw(self, amount): 
        newBalance = self._balance - amount

        if newBalance < self.__minimumBalance:
            return False

        self._balance = newBalance

        transaction = f"[{datetime.date.today()}] Withdrawal: -${amount:0.2f}"
        self.addTransaction(transaction)
        return True

        
    def applyInterest(self):
        interestAmount = self._balance * (self.__interestRate)
        self._balance = self._balance + interestAmount

        transaction = f"[{datetime.date.today()}] Interest applied: +${interestAmount:0.2f}"
        self.addTransaction(transaction)


    def getAccountType(self):
        return "Savings Account"

    


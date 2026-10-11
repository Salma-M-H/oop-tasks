from BankAccount import BankAccount
import datetime

class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, accountHolder, balance, overdraftLimit=500, transactionFee=0.5):
        super().__init__(accountNumber, accountHolder, balance)

        self.__overdraftLimit = overdraftLimit
        self.__transactionFee = transactionFee


    def withdraw(self, amount):
        newBalance = self._balance - amount

        if newBalance < -self.__overdraftLimit:
            return False

        self._balance = newBalance
        transaction = f"[{datetime.date.today()}] Withdrawal: -${amount:0.2f}"
        self.addTransaction(transaction)

        return True
        
    def chargeTransactionFee(self):
        newBalance = self._balance - self.__transactionFee
        self._balance = newBalance
        
        transaction = f"[{datetime.date.today()}] Transaction Fees: -${self.__transactionFee:0.2f}"
        self.addTransaction(transaction)

    def getAccountType(self):
        return "Checking Account"
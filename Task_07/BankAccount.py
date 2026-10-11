import datetime
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, accountNumber, accountHolder, balance):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self._balance = balance
        self.__transactions = []

    @property
    def accountNumber(self):
        return self.__accountNumber

    @property
    def accountHolder(self):
        return self.__accountHolder

    def deposit(self, amount):
        if amount <= 0:
            return 
        self._balance += amount
        transaction = f"[{datetime.date.today()}] Deposit: +${amount:0.2f}"
        self.addTransaction(transaction)

    @abstractmethod
    def withdraw(self, amount):
        return 

    def getBalance(self):
        return self._balance

    def getAccountInfo(self): 
        accountNumber = f"Account Number: {self.__accountNumber}\n"
        accountHolder = f"Name: {self.__accountHolder}\n"
        balance = f"Balance: {self._balance:0.2f}\n"
        text = accountNumber + accountHolder + balance
        return text

    def addTransaction(self, transaction):
        self.__transactions.append(transaction)

    def displayTransactionHistory(self):
        text = f"=== Transaction History for Account {self.__accountNumber} ===\n"
        for transaction in self.__transactions:
            text = text + transaction + "\n"

        print(text)



    
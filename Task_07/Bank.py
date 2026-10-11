from SavingAccount import SavingsAccount
from CheckingAccount import CheckingAccount
import datetime

class Bank:
    def __init__(self, bankName):
        self.__bankName = bankName
        self.__accounts = []

    def createSavingsAccount(self, holder, initialDeposit):
        accountNumber = f"{1001 + len(self.__accounts)}"
        accountHolder = holder
        balance = initialDeposit

        account = SavingsAccount(accountNumber, accountHolder, balance)

        transaction = f"[{datetime.date.today()}] Account opened with ${account.getBalance():0.2f}"
        account.addTransaction(transaction)

        self.__accounts.append(account)

        return account



    def createCheckingAccount(self, holder, initialDeposit):
        accountNumber = f"{1001 + len(self.__accounts)}"
        accountHolder = holder
        balance = initialDeposit

        account = CheckingAccount(accountNumber, accountHolder, balance)
        transaction = f"[{datetime.date.today()}] Account opened with ${account.getBalance():0.2f}"
        account.addTransaction(transaction)
        
        self.__accounts.append(account)

        return account



    def findAccount(self, accountNumber):
        for account in self.__accounts:
            if account.accountNumber.lower()== accountNumber.lower():
                return account


    def displayAllAccounts(self):
        print(f'=== All Accounts in {self.__bankName} ===')
        for account in self.__accounts:
            print(f'Account: {account.accountNumber} - {account.accountHolder} ({account.getAccountType()})')
            print(f'Balance: ${account.getBalance():0.2f}\n')

        
    def getTotalBankBalance(self):
        totalBalance = 0

        for account in self.__accounts:
            totalBalance += account.getBalance()
        return totalBalance
from Bank import Bank

bank = Bank('First National Bank')

savings = bank.createSavingsAccount("Alice Johnson", 1000.00)
checking = bank.createCheckingAccount("Bob Smith", 500.00)

bank.displayAllAccounts()

savings.deposit(500.00)
print(f"Alice's balance: ${savings.getBalance():0.2f}")

success = savings.withdraw(200.00)
if success:
    print("Withdrawal successful!")

success = savings.withdraw(1500.00)
if not success:
    print("Withdrawal failed: Would exceed minimum balance requirement")

savings.applyInterest()
print(f"After interest: ${savings.getBalance():0.2f}")

checking.withdraw(800.00) 
print(f"Bob's balance: ${checking.getBalance():0.2f}")

savings.displayTransactionHistory()

print(f"Total bank balance: ${bank.getTotalBankBalance():0.2f}")
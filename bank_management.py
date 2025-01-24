class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

class Account:
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.balance = 0.0
        self.transactions = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))
        print(f"Deposited {amount} into account {self.account_number}")
        print(f"New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw", amount))
            print(f"Withdrew {amount} from account {self.account_number}")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient balance!")
    
    def view_statement(self):
        print(f"\nBank Statement for Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: {self.balance}")
        print("\nTransactions:")
        for transaction in self.transactions:
            print(f"{transaction.transaction_type}: {transaction.amount}")

class Bank:
    def __init__(self):
        self.accounts = []
    
    def create_account(self):
        account_number = int(input("\nEnter account number: "))
        name = input("Enter account holder's name: ")
        new_account = Account(account_number, name)
        self.accounts.append(new_account)
        print("Account created successfully!")
    
    def view_account(self):
        account_number = int(input("\nEnter account number to view: "))
        account = self.find_account(account_number)
        if account:
            print(f"\nAccount Number: {account.account_number}")
            print(f"Account Holder: {account.name}")
            print(f"Account Balance: {account.balance}")
        else:
            print("Account not found!")
    
    def deposit_money(self):
        account_number = int(input("\nEnter account number to deposit into: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("Account not found!")
    
    def withdraw_money(self):
        account_number = int(input("\nEnter account number to withdraw from: "))
        account = self.find_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found!")
    
    def view_bank_statement(self):
        account_number = int(input("\nEnter account number to view bank statement: "))
        account = self.find_account(account_number)
        if account:
            account.view_statement()
        else:
            print("Account not found!")
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

def display_menu(bank):
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create a new account")
        print("2. View account details")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. View bank statement")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            bank.create_account()
        elif choice == 2:
            bank.view_account()
        elif choice == 3:
            bank.deposit_money()
        elif choice == 4:
            bank.withdraw_money()
        elif choice == 5:
            bank.view_bank_statement()
        elif choice == 6:
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    bank = Bank()
    display_menu(bank)

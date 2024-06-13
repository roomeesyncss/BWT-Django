class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n${amount:.2f} deposited successfully. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\n${amount:.2f} withdrawn successfully. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"\nAccount for {account.account_holder} added successfully.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def list_accounts(self):
        if not self.accounts:
            print("\nNo accounts in the bank.")
        else:
            print("\nListing all accounts:")
            for account in self.accounts:
                print(account)

def display_menu():
    print("\n--- Welcome to the Banking System ---")
    print("1. Add a New Account")
    print("2. Deposit to an Account")
    print("3. Withdraw from an Account")
    print("4. Check Account Balance")
    print("5. List All Accounts")
    print("6. Exit")

def main():
    bank = Bank()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            account_number = int(input("Enter Account Number: "))
            account_holder = input("Enter Account Holder Name: ").strip()
            initial_balance = float(input("Enter Initial Balance: "))
            new_account = Account(account_number, account_holder, initial_balance)
            bank.add_account(new_account)

        elif choice == '2':
            account_number = int(input("Enter Account Number for Deposit: "))
            amount = float(input("Enter Amount to Deposit: "))
            account = bank.find_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = int(input("Enter Account Number for Withdrawal: "))
            amount = float(input("Enter Amount to Withdraw: "))
            account = bank.find_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = int(input("Enter Account Number to Check Balance: "))
            account = bank.find_account(account_number)
            if account:
                print(f"\nBalance for {account.account_holder}'s account: ${account.get_balance():.2f}")
            else:
                print("Account not found.")

        elif choice == '5':
            bank.list_accounts()

        elif choice == '6':
            print("Exiting the Banking System. Have a nice day!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

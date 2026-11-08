class BankAcct:

#Creates all the parts needed for the account
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

#Changes the rate of interest if needed
    def change_interest_rate(self, new_rate):
        self.interest_rate = new_rate

#Accepts deposits as long as greater than 0
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.amount += deposit_amount
            print(f"${deposit_amount:.2f} deposited successfully.")
        else:
            print("Deposit amount can't be less than or equal to zero.")

#Accepts Withdraws as long as they are greater than 0
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0 and withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print(f"${withdraw_amount:.2f} withdrawn successfully.")
        else:
            print("Withdraw amount can't be less than or equal to zero.")

#Gets the account balance
    def get_balance(self):
        return self.amount

#Calculates interest for the account depending on how many days have passed
    def calculate_interest(self, days):
        interest= self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

#Displays the account information
    def __str__(self):
        interest = self.calculate_interest(365)

        return (
            f"Name: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Amount: {self.amount:.2f}\n"
            f"Interest: {self.interest_rate}%\n"
            f"Interest Earned (365 days): ${interest:.2f}"
        )

#Displays all the bank account information with transactions, interest rate, interest.
account1 = BankAcct("Chris Innes", 1234567890, 5000.00, 5.0)
account1.deposit(100)
account1.withdraw(600)
account1.change_interest_rate(6.5)
print("Current Balance:", account1.get_balance())
print(f"90 Day Interest: {account1.calculate_interest(90):.2f}")
print("\nAccount Info:")
print(account1)
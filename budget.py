class Budget:
    active_balance = 100000  # this is the account for deposit, withdraw on budgets
    savings_balance = 500000  # this is account for transferring to the "active_balance"

    def __init__(self, item, deposit_value, withdraw_value, transfer):
        self.item = item
        self.deposit_value = deposit_value
        self.withdraw_value = withdraw_value
        self.transfer = transfer

    def deposit(self):
        Budget.active_balance += self.deposit_value
        return f"You have deposited ${self.deposit_value} for {self.item}.Your balance is: ${Budget.active_balance} "

    def withdraw(self):
        Budget.active_balance -= self.withdraw_value
        return f"You have withdraw ${self.withdraw_value} for {self.item}.Your balance is: ${Budget.active_balance} "

    def balance(self):
        Budget.active_balance += 0
        print(f"Your current balance: ${Budget.active_balance}")
        Budget.active_balance += self.transfer
        Budget.savings_balance -= self.transfer
        return f"You have successfully transferred ${self.transfer} to the Current balance.\nTotal balance: ${Budget.active_balance} and Saving Balance: ${Budget.savings_balance}"


print(f"Your Current balance: ${Budget.active_balance}")
print(f"Your Savings balance: ${Budget.savings_balance}")
budget1 = Budget("Food", 20000, 4000, 90000)
budget2 = Budget("Clothing", 40000, 50000, 90000)

# This runs for the budget1
print(budget1.deposit())
print(budget1.withdraw())
print(budget1.balance())

# This runs for the budget2
"""
print(budget2.deposit())
print(budget2.withdraw())
print(budget2.balance())"""

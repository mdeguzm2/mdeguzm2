#BankAccount class
class BankAccount:
    bank_title = "Bank of America"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount
        print("Successfully deposited $" + str(amount))

    def withdraw(self, amount):
        if (self.current_balance-self.minimum_balance) >= amount:
            self.current_balance -= amount
            print("Successfully withdrawn $" + str(amount))
        else:
            print("Could not withdraw $" + str(amount) + ", current balance is only $" + str(self.current_balance) + ".")

    def print_customer_information(self):
        print("Bank Name: ", self.bank_title)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance, "\n")


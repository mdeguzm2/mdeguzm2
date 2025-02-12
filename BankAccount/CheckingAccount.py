from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, maximum_transfer):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.maximum_transfer = maximum_transfer

    def withdraw(self, amount):
        if ((self.current_balance-self.minimum_balance) >= amount) and (amount <= self.maximum_transfer):
            self.current_balance -= amount
            print("Successfully withdrawn $" + str(amount))
        else:
            print("Could not withdraw due to reaching below minimum balance or withdrawing"
                  " more than maximum transfer")

    def print_customer_information(self):
        super().print_customer_information()
        print("Maximum transfer limit: $" + str(self.maximum_transfer))
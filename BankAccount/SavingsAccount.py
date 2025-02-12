from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def print_customer_information(self):
        super().print_customer_information()
        print("Interest Rate: {}".format(self.interest_rate))
        print("Balance after next month: {}".format(self.current_balance*(1+self.interest_rate)))

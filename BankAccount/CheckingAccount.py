import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, maximum_transfer):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.maximum_transfer = maximum_transfer
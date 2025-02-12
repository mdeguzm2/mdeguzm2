#BankAccount1 class

class BankAccount:
    bank_title = "Bank of America"
    _account_number = 0
    __routing_number = 0

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
            print("Could not withdraw due to reaching below minimum balance")

    def print_customer_information(self):
        print("Bank Name: ", self.bank_title)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)

    def get_routing_number(self):
        return self.__routing_number

    def set_routing_number(self, routing_number):
        self.__routing_number = routing_number

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number




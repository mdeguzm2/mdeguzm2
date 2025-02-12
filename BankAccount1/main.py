import BankAccount

#creating instances
print("First instance, withdraw amount less than or equal to current balance:")
b1 = BankAccount("Matthew Deguzman", 1000.00, 100.00)
b1.deposit(200)
b1.withdraw(100)
b1.print_customer_information()

print("Second instance, withdraw amount greater than current balance:")
b2 = BankAccount("Test account 2", 684.29, 213.70)
b2.deposit(400)
b2.withdraw(2000)
b2.print_customer_information()
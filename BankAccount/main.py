from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

#creating instances
checking_account = CheckingAccount("checking", 1000, 100, 500)
print("Checking Account Initial Details:")
checking_account.print_customer_information()

checking_account.deposit(200)
checking_account.withdraw(300)
checking_account.withdraw(600)
checking_account.withdraw(950)

# Set and Get Routing/Account Numbers for Checking Account
checking_account.set_routing_number(111222333)
checking_account.set_account_number(444555666)
print("\nChecking Account - Updated Account Numbers:")
print("  Routing Number:", checking_account.get_routing_number())
print("  Account Number:", checking_account.get_account_number())

print("\nChecking Account Updated Details:")
checking_account.print_customer_information()

savings_account = SavingsAccount("savings", 2000, 200, 0.02)
print("\nSavings Account Initial Details:")
savings_account.print_customer_information()

savings_account.deposit(500)

# Set and Get Routing/Account Numbers for Savings Account
savings_account.set_routing_number(999888777)
savings_account.set_account_number(666555444)
print("\nSavings Account - Updated Account Numbers:")
print("  Routing Number:", savings_account.get_routing_number())
print("  Account Number:", savings_account.get_account_number())

print("\nSavings Account Updated Details:")
savings_account.print_customer_information()

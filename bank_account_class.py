"""
Bank Account

NOTE: This exercise is divided into different parts. You'll need to complete them in order.
"""

"""
1. Create an `Account` class to represent unique bank accounts.

Ensure that when you create a new instance of `Account`, that instances has attributes for the bank account number, account owner's name, and the initial balance. Use your best judgement when deciding the attribute names.

It should have a class attribute for the default interest rate on a general account - you can use 2.25 for the interest rate.

Add an instance method called `acc_details` that prints out all these account details. Then, create at least once instance and print out its details.
"""

"""
2. Write and call a method `deposit()` that allows you to deposit money into the instance of `Account`. It should update the current account balance; record the transaction in an attribute called `transactions` and print the record; and print out a deposit confirmation message.

You can format the transaction records like this - "Deposit: <starting balance>, <ending balance>"
You can format the deposit confirmation message like this - "$<amount> deposit complete."
"""

"""
3. Create a `SavingsAccount` class that inherits from the general `Account` class. It should have its own `int_rate` as a class attribute.

Create at least once instance of `SavingsAccount`, and call the `deposit` and `acc_details` methods on it.
"""

"""
4. Create a `CheckingAccount` class that inherits from the general `Account` class.

It should have its own `int_rate` as a class attribute. Also, add an `withdraw` instance method that behaves in the opposite manner of the `deposit` instance method defined on `Account`.

Create at least once instance of `CheckingAccount`, and call both the `deposit` and `withdraw` methods on it.
"""
class Account:
    int_rate = 2.25

    def __init__(self,account_number,first_name,last_name,balance):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
    
    
    def acc_details(self):
        account_details = {
            'Account Number': self.account_number,
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Initial Balance': self.balance
        }
        for details, keys in account_details.items():
            print("{}: {}".format(details, keys))
        return ""

    def deposit(self, transactions):
        new_balance = self.balance + transactions
        amount = new_balance
        print(f"Deposit:< Starting Balance> ${self.balance}, <Ending Balance> ${new_balance}")
        print(f"${amount} deposit complete")

class SavingsAccount(Account):
    int_rate = 2.50


class CheckingAccount(Account):
    int_rate = 1.25
    
    def withdraw(self,withdraw):
        new_balance = self.balance - withdraw
        print(f"Initial Balance: ${self.balance}, Ending Balance: ${new_balance}")




account_1 = Account(1234, "James", "Cook", 400)

print(account_1.acc_details())

account_1.deposit(200)
print("------------------------------------------")
savings_account_1 = SavingsAccount(2345, "Sam", "Krane", 500)

print(savings_account_1.acc_details())

savings_account_1.deposit(600)
print("-------------------------------------------")
checking_account_1 = CheckingAccount(4567, "Drew", "Sanders", 600)

checking_account_1.acc_details()

checking_account_1.deposit(400)

checking_account_1.withdraw(200)






       

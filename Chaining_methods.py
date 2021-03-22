#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
#display_user_balance(self) - have this method print the user's name and account balance to the terminal
#eg. "User: Guido van Rossum, Balance: $150
#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
# Adding a deposit function
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
# Adding a withdrawal function
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
# Adding a display user balance function
    def display_user_balance(self):
        print(f"User {self.name} has the balance of {self.account_balance} dollars.")
        return self
# BONUS Adding a transfer function
    def transfer_money(self, secondary_user, amount):
        self.account_balance -= amount
        secondary_user.account_balance += amount
        return self
# Creating users (instances)
ramon = User("Ramon O. Mallari Jr.", "ramon.mallari@gmail.com")
kristine = User("Kristin May P. Mallari", "kristinemaypinsan@gmail.com")
zoe = User("Zoe Skylar P. Mallari", "zoe.mallari@gmail.com")

#print(ramon.name)
#print(kristine.name)
#print(zoe.name)
# Making deposits
ramon.make_deposit(100).make_deposit(200).make_deposit(500).make_withdrawal(100).display_user_balance()
kristine.make_deposit(50).make_deposit(700).make_withdrawal(25).make_withdrawal(73).display_user_balance()
zoe.make_deposit(1500).make_withdrawal(23).make_withdrawal(71).make_withdrawal(762).display_user_balance()
#print(ramon.account_balance)
#print(kristine.account_balance)
ramon.transfer_money(zoe,200).display_user_balance()
zoe.display_user_balance()


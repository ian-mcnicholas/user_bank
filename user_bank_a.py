class BankAccount:
    
   
    # don't forget to add some default values for these parameters!
    def __init__(self, balance = 0, int_rate = 0.05, name =""): 
        self.balance = balance
        self.int_rate = int_rate
        self.name = name
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here
    def display_account_info(self):
        print(f'Your balance is: {self.balance} , Your interest rate is {self.int_rate}')
        return self
        # your code here
    def yield_interest(self):
        self.balance *= (1+ self.int_rate)
        return self


# Update the User class __init__ method

# Update the User class make_deposit method

# Update the User class make_withdrawal method

# Update the User class display_user_balance method

class user:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.account = BankAccount(balance = 0, int_rate = 0.05, name ="")
        

    def make_deposit(self, amount):
        self.account.deposit(amount) # += amount take out because of function
        return(self)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount) 
        return(self)

    def new_display(self):
        
        print(f"User: {self.name}, User Id: {self.uid}") # Current Balance: {self.account.balance} ")
        self.account.display_account_info()
        return(self)

user1 = user("JJ496", "John Account")

user1.make_deposit(500).make_deposit(10000).make_deposit(100).make_withdrawal(65).new_display()

user2 = user("SDash76", "Stacy Account")

user2.make_deposit(50878760).make_deposit(10000).make_deposit(100).make_withdrawal(500065).new_display()
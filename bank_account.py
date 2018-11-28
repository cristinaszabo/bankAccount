#this is only good when u create accounts, i don't know what to do when the account exist and there is a balance already

class BankAccount:
    def __init__(self,name_account):
        self.name=name_account
        self.rate=0.05
        self.balance=0
    #add method deposit
    def deposit(self,amount):
        self.balance+=amount
        return self
    #add method withdrawal
    def withdrawal(self,amount):
        if amount>self.balance:
            print("\nAccount",self.name," has Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-amount-5
        else: 
            self.balance-=amount
        return self
    #add display account info method
    def display_account_info(self):
        print("Account",self.name,"has a Balance: $",self.balance)
        return self
    #add interest method
    def yeld_interest(self):
        if self.balance>0:
            self.balance=self.balance+self.balance*self.rate
        return self
# create 2 account
guido=BankAccount("Guido van Rosa")
kris=BankAccount("Kris Cross")

#make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
guido.deposit(100).deposit(200).deposit(800).withdrawal(500).yeld_interest().display_account_info()
#make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
kris.deposit(100).deposit(250).withdrawal(150).withdrawal(50).withdrawal(100).withdrawal(100).yeld_interest().display_account_info()
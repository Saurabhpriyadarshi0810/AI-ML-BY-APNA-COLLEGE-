class Bank_account:
    account_no = 0
    owner_name = ""
    balance = 0

    def __init__ (self , acc_no , name  , balance ):
        self.owner_name = name 
        self.balance = balance
        self.account_no = acc_no

    def deposit(self, amount):
        if amount < 0 :
            print( " invalid amount !")
        else:
            self.balance  = self.balance + amount
            print(f"{amount} is successfully deposited in your bank account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficent balance !")
        else:
            self.balance  -= amount
            print(f"{amount} is successfully credited from your bank account.")

    def check_balance(self):
        
        print(f"current available balance = {self.balance}.")


b=Bank_account(1254 , "Saurabh " , 100000)
b.deposit(1000)
b.withdraw(500)
b.check_balance()
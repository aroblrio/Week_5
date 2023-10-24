
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def get_account_number(self):
        print(self.account_number)
        return self.account_number
    def get_balance(self):
        #print(self.balance)
        return self.balance
    def add_funds(self,funds):
        self.balance = self.balance + funds
    def add_withdraws(self,funds):
        self.balance = self.balance - funds
"""
cuenta1 = BankAccount('ES12', 300)
cuenta1.get_account_number()
cuenta1.get_balance()
cuenta1.add_funds(650)
cuenta1.add_withdraws(1000)
cuenta1.get_balance()

 """       
    

    














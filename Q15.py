class BankAccout():
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('You have deposited Rs.{} and your new balance is Rs.{}'.format(amount,self.balance))

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
            print('You have withdrawn Rs.{} and your new balance is Rs.{}'.format(amount,self.balance))
        else:
            print('You don\'t have enough amount to withdraw' )

customer=BankAccout()
customer.deposit(1000)
customer.withdraw(500)
customer.withdraw(100)
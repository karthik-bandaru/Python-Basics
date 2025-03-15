class BankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.__balance = balance

    def get_bankBalance(self):
        return "Your Cuurent Bank Balance is ",self.__balance
    
    def desposit(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            print("Deposit the amount correctly..!")

    def withdraw(self,amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
        else:
            print("Enter Correct money for Withdraw..!")

inst = BankAccount("Karthii",1500)
inst.get_bankBalance()
inst.desposit(500)
inst.get_bankBalance()
inst.withdraw(200)
inst.get_bankBalance()

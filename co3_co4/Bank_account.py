class bankaccount():
    def __init__(self,a,b,c):
        self.balance=0
        self.name=a
        self.number=b
        self.type=c
    print("welcome to CASH DEPO-WID SYSTEM")
    def bankname(self):
        print("bank name is ",self.name)
        print("Bank number is ",self.number)
        print("account type is ",self.type)

    def deposit(self):
        amount=float(input("Enter the amount to be deposited: "))
        self.balance+=amount
        print(amount," Deposited")

    def withdraw(self):
        amount=float(input("Enter the amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print(amount," Withdrawn")
        else:
            print("Insufficient Balance")

    def display(self):
        print(" Net Available Balance=", self.balance)


abankname=input("Enter your bank name: ")
abankno=input("Enter your account number")
abanktype=input("Enter your acc type--savings/current")
s=bankaccount(abankname,abankno,abanktype)
s.bankname()
s.deposit()
s.withdraw()
s.display()



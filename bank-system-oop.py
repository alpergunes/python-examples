class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print(f'Personal Details\n\nName:{self.name}\nAge:{self.age}\nGender:{self.age}')
alper = User('alper',21,'E')
alper.show_details()

class Bank(User):
    def __init__(self,name,age,gender,):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Acount balance has been updated: ${self.balance}')
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print(f'Insufficient Funds | Balance Available: ${self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'Account balance has been updated $ {self.balance}')
    def view_balance(self):
        self.show_details()
        print(f'Account balance has been updated $ {self.balance}')




alper = Bank('alper',21,'E')

alper.deposit(1000)

alper.withdraw(900)

alper.view_balance()
#Adult class



class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print('Personal Details')
        print('')
        print('Name', self.name)
        print('Age', self.age)
        print('Gender', self.gender)

yavuz = User('Yavuz', 20, 'Male')
yavuz.show_details()

#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        print('Account balance has been updated: £', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('Insufficient Funds | Balance Avaible: £', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Account balance has been updated', self.balance)

kerim = Bank('Kerim', 15, 'Mollahamzaoğlu') 
kerim.name
kerim.age
kerim.deposit(200)
kerim.deposit(600)
kerim.withdraw(500)
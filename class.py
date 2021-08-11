'''class Circle:

    pi = 3.14
    
    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    def cevre_hesapla(self):
            return 2*self.pi + self.yaricap
    
    def alan_hesapla(self):
            return self.pi* (self.yaricap**2)
            

c1 = Circle() #yaricap = 1
c2 = Circle(5)

print(f'c1 :  alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2 :  alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')'''

'''class calisan:        #yanlış class yapısı
    pass
calisan1 = calisan()
calisan1.name = 'Yavuz'
calisan1.surname = 'Molla'
calisan1.age = 20
print(calisan1.name)
print(calisan1.surname)
calisan2 = calisan()
calisan2.email = 'a@fdsafa.com'
print(calisan2.email)'''


'''class calisan:
    def __init__(self,name,surname = 'girilmedi',age = 0):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f'Name:{self.name} Surname: {self.surname} Age: {self.age}')

calisan1 = calisan('Yavuz','Molla',)
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 = calisan('Havva','Molla','50')
print(calisan2.name,calisan2.surname,calisan2.age)


calisan1.show_info()
calisan2.show_info()


calisan.show_info(calisan1)'''


'''class calisan:
    personel_sayisi = 0
    zam_orani = 1.1
    def __init__(self,isim,maas):
        

        self.isim = isim 
        self.maas = maas
        calisan.personel_sayisi += 1
worker1 = calisan('Ali',2000)
worker2 = calisan('Yavuz',6000)

worker1.zam_orani = 1.2
print(calisan.zam_orani)


print(calisan.zam_orani)
print(worker2.zam_orani)

print(worker1.isim,worker1.maas)
print(worker2.isim,worker2.maas)

print(calisan.__dict__)
print(worker1.__dict__)
print(worker2.__dict__)'''



#Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()

#Student(Person), Teacher(Person)

#Animal => Dog(Animal), Cat(Animal)

'''class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastname = lname
        print('^Person Created')
    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('Student Created')
        
    def who_am_i(self):
        print('I am a student')


p1 = Person('Yavuz', 'Molla')
s1 = Student('Betül', 'Molla')
print(p1.firstName + ''+ p1.lastname)
print(s1.firstName + ''+ s1.lastname)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.who_am_i()'''


myList = [1,2,3]
myString = 'My string'

print(len(myList))
print(len(myString))

class Movie():
    pass

m = Movie()
print(type(m))
print(len(m))










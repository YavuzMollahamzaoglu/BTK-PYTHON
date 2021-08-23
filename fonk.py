# def greeting(name):
#     print('hello', name)

# print(greeting('ali'))
# print(greeting)

# sayHello = greeting

# print(greeting('Yavuz'))
# print(sayHello)
# print(greeting)

# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)

# outer(10)
# #inner_increment(10)


# def factorial(number):

#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)

# print(factorial(5))

# def usalma(number):
#     # two = usalma(2)
#     # three = usalma(3)

#     def inner(power):
#         return number ** power

#     return inner
# two = usalma(2)
# print(two(3))
# three = usalma(3)

# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return '{0} rolünün {1} sayfasına ulaşabilir '.format(role)
#         else:
#             return '{0} rolünün {1} sayfasına ulaşamaz '.format(role)
#     return inner
# user1 = yetki_sorgula('Product Edit')
# print(user1('Admin'))
# print(user1('User'))



# def islem(islem_adi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam+=i
#         return toplam

#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim*=i
#         return carpim
#     if islem_adi == 'toplam':
#         return toplam
#     else:
#         return carpma


def dis_fonk():
    print('Dış fonk çalışıyor')
    def ic_fonk():
        print('İç fonk çalışıyor')

    print('Dış fonk sonlanıyor')
    # ic_fonk()
# dis_fonk()

def hesaplamalar(x):
    def kare_al(a):
        return a ** 2
    def karekok_al(a):
        return a ** 0.5
    def faktoriyel(a):
        carpim = 1
        for i in range(1, a + 1):
            carpim *= i
            return carpim
    kare = kare_al(x)
    karekok = karekok_al(x)
    fakt = faktoriyel(x)

    return f'Karesi: {kare} Karekökü: {karekok} Faktöriyel: {fakt} '


print(hesaplamalar(6))

'''def sayHello(name = 'User'):
    print('Hello' + name)

sayHello('Yavuz')
sayHello('Havva')
sayHello()'''
 # dışardan bilgi göndermek yerine return ifadesi ile istedğimiz sınıfta değeri verelim .



'''def sayHello(name = 'user'):
     return 'Hello' + name

msg = sayHello('Çınar')

print(msg)


def total(num1, num2):
    return num1 + num2

result = total(10,20)
print(result)'''
 

def yasHesapla(dogumYili):
    return 2019 - dogumYili

ageYavuz = yasHesapla(2017)
ageHavva = yasHesapla(1970)

print(ageHavva,ageYavuz)



def EmekliligeKacYilKaldi(dogumYili, isim):
    
    yas = yasHesapla(dogumYili)

    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı' )
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(1983, 'Ali')
'''def changeName(n):
    n = 'Yavuz'

name = 'Havva'

changeName(name)
print(name)

def change(n):
    n[0] = 'Mersin'

sehirler = ['ankara', 'ıstanbul']

#n = sehirler[0:2]           #burdaki işlemle 0 ve 2 arasındaki hepsini silmemizi sağlar . slicing anlamıba gelir 


change(sehirler)

print(sehirler)


def add(a, b):
    return sum((a,b))               #sum() fonksiyonu parametleri toplamya yarar .

print(add(10, 20))                      '''

'''def displayUser(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Çınar', age = 2, city = 'Mersin')'''


'''def topla(sayi1, sayi2=3):          #burda 2. parametre değer vermesekte 3 olarak yazılcak yani hata vermeyecek . Ama değer verirsek verdiğimizi yazar .
    print('sayi1:', sayi1)
    print('sayi2:', sayi2)
    return sayi1 + sayi2

print(topla(5))'''

'''def topla(sayi1, sayi2=3, sayi3=5):
    print('sayi1:', sayi1, 'sayi2:', sayi2, 'sayi3:', sayi3)
    return sayi3+sayi1+sayi2

print(topla(5, 2, 3))
print(topla(5, sayi3=5)) '''        # direk 2 yi vermeden 3'ü vermek için tanımladığımız değikeni yazmamız lazım.



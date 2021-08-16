#Dosya açmak ve oluşturmak için ()open fonksiyonu kullanılır.
#Kullanımı: open(dosya_adi,dosya_erişme_modu)
#dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.


#'w': (Write) yazma modu. Dosyayı konumda oluşturur.
#  ** Dosyayı konumda oluşturur.
#  ** Dosya içeriğini siler ve yeniden ekleme yapar.
#result = open('newfile.txt','w')
#file.close()
#print(result)


#file = open('newfile.txt','w',encoding='utf-8')    # 3. da yazdığımız şey tanınmayan karakterleri tanır.
#file.write('Yavuz Mollahamzaoğlu')
#file.close()


#'a' (Append) ekleme. Dosya konumda yoksa oluşturur.
#file = open('newfile.txt','a',encoding='utf-8')
#file.write('\nHavva Mollahamzaoğlu')
#file.close


#'x' (Create) oluşturma. Dosya zaten varsa hata verir.
#file = open('newfile2.txt','x',encoding='utf-8')


#'r' (Read) okuma. varsayılan dosya konumunda yoksa hata verir.
# try:
#     file = open('newfile.txt')
#     print(file)
# except FileNotFoundError:
#     print('Dosya okuma hatası.')
# finally:
#     print('Dosya kapandı')
#     file.close()

from os import close, write


file = open('newfile.txt','r', encoding='utf-8')

# for döngüsü

# for i in file:
#     print(i, end='')

#read() fonksiyonu
# content1 = file.read()
# print('İçerik 1')
# print(content1)
# content2 = file.read()

# print('İçerik 2')
# print(content2)
# file.close()


# ******************readline() fonksiyonu
# print(file.readline(),end='')
# print(file.readline(),end='')
# file.close()



#************ readlines() fonksiyonu

# liste = file.readlines()

# print(liste)

# file.close()


# with  open('newfile.txt','r',encoding=('utf-8') as file:
#     content = file.read()
#     print(content)
#     print(file.tell())

# Dosyada güncelleme yapma
# with open('newfile.txt','r+',encoding='utf-8') as file:
#     file.seek(20)
#     file.write('Deneme')

# with open('newfile.txt','r+',encoding='utf-8') as file:
#     print(file.read())


# with open('newfile.txt','a',encoding='utf-8') as file:
#     file.write('\n Gül Keniş')
#****** Sayfa başında güncelleme
# with open('newfile.txt','r+',encoding='utf-8') as file:
#     content = file.read()
#     content = 'Efe Kasap\n' + content 
#     file.seek(0)
#     file.write(content)

#****** Sayfa ortasında güncelleme 
with open('newfile.txt','r+',encoding='utf-8') as file:
    list = file.readlines()
    list.insert(1,'Betül Mollahamzaoğlu')
    file.seek(0)
    for i in list:
        file.write(i)

with  open('newfile.txt','r',encoding='utf-8') as file:
    print(file.read())





# with open('newfile.txt','r',encoding='utf-8') as file:
#     print(file.read())

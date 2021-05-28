message = 'Hello There. My name is Yavuz Mollahamzaoğlu'

#message = message.upper()
# message =message.lower()
# message = message.title()   # her başlangıçı büyük yapar .
# message = message.capitalize()     #sadece başlangıç kelmesini büyük başlatır.

'''message = message.strip()'''   #baş ve sondak boşluk karakterleri siler .

'''message = message.split()'''       #içindeki karakterlerin ayrılmasını sağlar .

# message = message.split('.')        # ordaki nokta sayesinde kelimeleri noktadan itibaren ayırcak.

# '''message = ' '.join(message)'''       # parçaları birleştirmeyi sağlar veverdiğimiz boşluk sayesinde aralara boşluk koyar.

# print(message)
# print(message[0])

# index = message.find('Yavuz')        # aradığımız kelimeyi bulmayı sağlar.
# print(index)
# print(message)


# message = message.replace('Yavuz', 'Havva')       # yerleri değiştirmeye yarar 
# print(message)


message = message.center(100,'*')         # 100 karakterlik bir alan oluşturdu .
print(message)



# .startswith() neyle başladığını sorgular.      .endswith   ise neyle bittiğini sorgular .,,
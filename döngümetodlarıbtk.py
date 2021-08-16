'''for i in range(2,10):
    print(i)'''

'''for item in range(50,100,20)
    print(item)


print(list(range(5,100,10)))'''


greeting = 'Hello There'
'''index = 0
for letter in  greeting:
    print(f'index: {index} letter: {letter}')

    index += 1'''

'''for item in enumerate(greeting):   #enumarate indexlerine göre sıralar
    print(f'index: {index} letter: {letter}')'''


list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1, list2)))      # zip karşılıklı olarak eşleştirir.


for item in zip(list1, list2):
    print(item)

for a,b,c in zip(list1, list2):
    print(a,b,c)


'''for x in range(10):
    print(x)

numbers =[x for x in range(10)]    #listeye alır 
print(numbers)

numbers = []
for x in range(10):
    numbers.append(x)     #listeye sokar 

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)'''


years = [1983,1999,2008,1956,1986]
ages = [ages - 2021 for year in years]
print(ages)


result = [x for x in range(1,10)]
results = [x if x %2==0 else 'TEK'for x in range(1,10)]

import random

#result = dir(random)
#print(result)
#result = help(random)
#print(result)

result = random.random()
print(result)

result = random.random() * 100
print(result)

result = random.uniform(1,10)
print(result)

result = random.randint(1,100)
print(result)

names = ['ali','yağmur','yavuz','gül']
result = names[random.randint(0,len(names) - 1)]
print(result)

greeting = ' Hello there'

result = random.choice(greeting)
print(result)

liste = list(range(10))
random.shuffle(liste)
result = liste

print(result)













#import math
#import math as islem
#value = dir(math)
#value = help(math)
#value = help(math.factorial)
#value = math.sqrt(49)
#value = math.factorial(5)
#value = math.floor(5.9)
#print(value)
#value = math.ceil(5.9)

#value = islem.factorial(5) # math modülünün ismini islem yaptık ve kullandık.

#from math import

#print(value)
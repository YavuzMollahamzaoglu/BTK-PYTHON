numbers = [1,2,3,4,5]

for i in numbers:
    print(i)
    print('Hello')


    names = ['yavuz', 'onur', 'gül']
    for name in names:
        print(f'my name is {name}')

name = 'Yavuz Molla'

for n in name:
    print(n)



tuple = (1,2,3,4,5)
for t in tuple:
    print(t)



tuple = [(1,2),(1,3,(1,4),(1,5)]     #hepsini ayrı ayrı yaazar .
for a,b in tuple:
    print(a)

d = {'k1':1, 'k2':2,'k3':3}
for item in d.items():                     #d.item yazmazisek sadece keyleri yazar valueleri vermez.
    print(item)

d = {'k1':1, 'k2':2,'k3':3}
for key,value in d.items():
    print(key, value)
    print(key)

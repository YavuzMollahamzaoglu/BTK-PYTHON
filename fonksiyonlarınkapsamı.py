'''#global scope

x = 'global x'

def function():
    #local scope
    x = 'local x'
    print(x)
function()
print(x)'''

'''name = 'Yavuz'
def changeName(new_name):
    name = new_name
    print(name)

changeName('Ada')
print(name)'''

'''name = 'Global string'         # sırasıyla isimleri içine koyar 
def greeting():
    name = 'Çınar'

    def hello():
        name = 'Ada'
        print('Hello' + name)

    hello()

greeting()'''


x = 50
def test(x):
    print('x' + x)
    x = 100
    print(f'changed x to  {x}')

test(x)
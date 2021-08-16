#print(a) => NameError
#int('1a2') => Value Error
#print(10/0) => ZeroDivisionError
#print('denem'e) => SyntaxError
# 
#
#
'''try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y için 0 girilemez')

except ValueError:
    print('x ve y için sayısal değer girmelisiniz')
else:
    print('Herşey yolunda')'''


try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except:
    print('Yanlış bilgi girdiniz')
else:
    break
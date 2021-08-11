def square(num): return num ** 2
numbers = [1,3,5,9]

result = list(map(square, numbers))
print(result)
result = square(2)
print(result)

for item in map(square, numbers):
    print(item)

result = list(map(lambda num: num ** 2, numbers))
print(result)


def check_even(num): return num%2==0

result = list(filter(check_even, numbers))
print(result)
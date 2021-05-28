numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a','s']

val = min(numbers)
val = max(numbers)

val = max(letters)
val = min(letters)
print(val)


val = numbers[3:6]

numbers[4] = 40

numbers.append('49')    # eklemeyi sağlar sona ekler.
numbers.insert(3, 78)  # istedğimiz indeksin yerine koyuyoruz
numbers.insert(-1, 52)
numbers.pop(0)    # indeksin listeden silinmesini sağlar

numbers.remove(52)    # aradığı sayıyı siler

numbers.sort()  #sayısal büyüklük olarak sıralanır
letters.sort() # alfabetik olarak sıralanır.        tersini yapmak için .revers() kullanılır.
print(numbers)


print(numbers.count(10))      # kaç  tane   10 bulunduğunu söyler.
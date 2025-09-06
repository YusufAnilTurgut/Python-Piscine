fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)          # ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi")
print(fruits)          # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana")
print(fruits)          # ['apple', 'kiwi', 'cherry', 'orange']

fruits.pop()           # son elemanı siler
print(fruits)          # ['apple', 'kiwi', 'cherry']


fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)          # ['apple', 'blueberry', 'cherry']


numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]
print(numbers[:3])     # [0, 1, 2]
print(numbers[3:])     # [3, 4, 5]

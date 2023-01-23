# Comprehension:
# [expression for item in items]

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


# With list comprehensions we can achieve the same result with a cleaner code

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] # List comprehension: cleaner and easy to understand
# both the above lines produce the same result

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10] # List comprehension: cleaner and readable
# both the above lines produce the same result


# Python program to demonstrate list comprehension in Python
# below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

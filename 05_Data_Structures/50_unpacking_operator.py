# unpacking operator : can unpack any iterable.

# Here we unpack the container, take out its individual elements and pass them as arbitrary arguments.

numbers = [1, 2, 3]
print(numbers)  # we get a list on the terminal [1, 2, 3]

# if we want to print the individual number like
print(1, 2, 3)  # 1 2 3

# we can use the unpacking operator to achieve this by prefixing the list variable with '*'
print(*numbers) # 1 2 3

# Another useful application of unpacking operator is when creating list
values = list(range(5))
print(values)
# instead of using list function, we can use unpacking operator on the range() iterable object
# or a string object (string is also iterable)
values = [*range(5), *"Hello"]
print(values)


# Another application : using unpacking operator, we can also combine multiple lists.
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)


# We can also unpack dictionaries, but for that we need '**'
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}  # unpack 'first', then 'second', add new key-value 'z'
print(combined) # output: {'x': 10, 'y': 2, 'z': 1}
# if we have multiple items with the same key, then the last value will be used.

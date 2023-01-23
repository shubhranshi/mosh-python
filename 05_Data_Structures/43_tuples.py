# Tuples: similar to list - tuples are read-only list, defined using parenthesis.
# but cannot be modified - they are immutable. Lists are mutable

numbers = (1, 2, 3)
print(numbers[0])

# numbers[0] = 10 ## this line gives error
# cannot be reassigned

# list are more often used than tuples.
# Tuples are useful when we don't want anyone to accidentally modify the contents.

point = 1, 2
print(type(point)) # <class 'tuple'>

point = ()
print(type(point)) # <class 'tuple'>

# just like lists, we can concat 2 tuples
point = (1, 2) + (3, 4)
print(point) # (1, 2, 3, 4)

point = (1, 2) * 3
print(point) # (1, 2, 1, 2, 1, 2) repeated tuple


# we can convert a list to a tuple
# tuple() function takes any iterable and converts it into a tuple
point = tuple([1, 2])
print(point)

point = tuple("Hello World")   # string is an iterable, can be converted to a tuple using built in tuple()
print(point)

# we can access values in the tuple
point = (1, 2, 3)

print(point[0:2])   # access values for a given index range

x, y, z = point     # unpack tuple into variables
print(x, y, z)

if 10 in point:     # use 'in' to check for item existence in tuple
    print("exists")

# we cannot add or remove objects/items in the tuple.

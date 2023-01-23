# python allows unpacking


coordinates = [1, 2, 3]
# coordinates = (1, 2, 3) # unpacking also works for tuples

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# can be re-written as
x, y, z = coordinates
print(y)
# The best way to this is by list unpacking
# The number of item on the left side of = must be the same as the number of items in the list.

full_name = ['rob', 'john']
f_name, l_name = full_name
print(l_name)


# number of variables on the left side should be equal to the elements in the list
# but if we just want only the first 2 or 3 values then we can write use *var_name
# *var_name packs all the other items in a separate list (packing)
numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 7]

# If we want to unpack the first two item and pack the rest of item in another list
first, second, *others = numbers
print(first)
print(second)
print(others)

# For example if we want to unpack the first and the last item
first, *others, last = numbers
print(first)
print(last)
print(others)

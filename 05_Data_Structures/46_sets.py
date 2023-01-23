# Python also includes a data type for sets.
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.

# sets is a type of collection with no duplicates
# sets are unordered collection

numbers = [1, 1, 2, 3, 3, 4, 2, 2, 5]

first = set(numbers)
print(first)      # {1, 2, 3, 4, 5}


# similar to lists, we can add new items, remove existing items
second = {1, 4, 6}

second.add(5)
second.remove(5)

print(second)
print(len(second))

# sets are quite powerful in the mathematical functions that it supports
# UNION
print(first | second)
print(first.union(second))

# INTERSECTION
print(first & second)
print(first.intersection(second))

# DIFFERENCE
print(first - second)
print(first.difference(second))
print(second - first)
print(second.difference(first))

# SYMMETRIC DIFFERENCE: returns items that are either in first or second set, but not in both
print(first ^ second)
print(first.symmetric_difference(second))

# we cannot access items in a set by using indexes because they are unordered collection
# print(first[0]) this will give error

# however we can check for an item existence in the set
if 4 in first:
    print("exists in first")
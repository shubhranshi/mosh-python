# Another scenario for using lambda functions:
# Lets say we have a list of items, and we want to filter this list.
# We want to get items with price >= 10
# we can use a filter() function for this
# filter() function takes a lambda function and a iterable
# it will apply this lambda function on each item of this iterable and
# if the item matches the criteria, it will be returned.

# In lambda item: item[1] >= 10
# the expression item[1] >= 10 gives a boolean value, so if it is True, this item will be returned.

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# the filter object is a iterable.
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
# [('Product1', 10), ('Product3', 12)]


# the filter object is a iterable.
maped = list(map(lambda item: item[1] >= 10, items))
print(maped)
# [True, False, True]
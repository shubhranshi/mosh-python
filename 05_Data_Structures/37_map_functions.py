# map our items list into a price list
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# Transform this list in a simple list of numbers, with just the price
# we want to get a list of prices

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# there is a better way to get this list of prices
# by using map() function
# map() takes 2 parameters: a function, and one or more iterable.

# this map() function will apply lambda function on each item in this list

x = map(lambda item: item[1], items)
# map() will iterate over items and call this lambda function item: item[1] on each item in the list
# map() returns an iterable map object
for item in x:
    print(item)

# directly convert this map object to a list object: using list(), list functions take any iterable.
prices = list(map(lambda item: item[1], items))
print(prices)
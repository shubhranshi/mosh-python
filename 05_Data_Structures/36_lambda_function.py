# lambda functions are simple one-line anonymous functions that we can pass to other functions.
# lambda parameters:expression

# List of complex objects, like a list of tuples, example a list of orders with product name and price
# in situations like this we need to define a function to sort the list, simple sort() method won't work
# In this example we are going to sort the items base in price
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]
# here the parameter is item
# and the expression (or the value we are calculating/returning) is item[1]


# with a lambda or anonymous functions it's short and cleaner way to define a function
# that we are going to use only once as an argument of another function.
# lambda parameter_list: expression
items.sort(key=lambda item:item[1])
print(items)


# ####################################################################################
# Python lambda properties:
# This function can have any number of arguments but only one expression, which is evaluated and returned.
# One is free to use lambda functions wherever function objects are required.
# You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
# It has various uses in particular fields of programming, besides other types of expressions in functions.

# More Examples:

# Example 1:

calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))


# Example 2: Program to demonstrate return type of Python lambda keyword

string = 'GeeksforGeeks'

# lambda returns a function object
print(lambda string: string)

# Output
# <function <lambda> at 0x7fd7517ade18>


# Example 3: Invoking lambda return value to perform various operations

filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

# Output
# filter_nums(): Geeks
# do_exclaim(): I am tired!
# find_sum(): 2


# Example 4:  Difference between lambda and normal function call

def cube(y):
	print(f"Finding cube of number:{y}")
	return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))

# Output
# invoking function defined with def keyword:
# Finding cube of number:30
# 27000
# invoking lambda function: 27000


# Example 5: The lambda function gets more helpful when used inside a function.

l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
	sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:",
	list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
	list(map(lambda x: str(int(x) + 10), l)))


# Output
# Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
# Filtered positive even numbers: ['1', '9', '0', '-1', '-2']
# Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']
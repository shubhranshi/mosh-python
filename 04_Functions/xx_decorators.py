# Decorators are a very powerful and useful tool in Python since it allows programmers to
# modify the behaviour of a function or class. Decorators allow us to wrap another function
# in order to extend the behaviour of the wrapped function, without permanently modifying it.

# In Decorators, functions are taken as the argument into another function and then called inside
# the wrapper function.

'''
@gfg_decorator
def hello_decorator():
    print("Gfg")
'''

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)'''


# In the above code, gfg_decorator is a callable function, that will add some code on the top of some
# another callable function, hello_decorator function and return the wrapper function.
# Decorator can modify the behaviour:

# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in which the argument is called
    # inner function can access the outer local functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

# Output
# Hello, this is before function execution
# This is inside the function !!
# This is after function execution


# Let’s jump to another example where we can easily find out the execution time of a function
# using a decorator.


# importing libraries
import time
import math


# decorator to calculate duration taken by any function.
def calculate_time(func):
    # added arguments inside the inner1, if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)

# Output
# 3628800
# Total time taken in :  factorial 2.0061802864074707


# What if a function returns something or an argument is passed to the function?
# In all the above examples the functions didn’t return anything so there wasn’t an issue,
# but one may need the returned value.

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

# Output
# before Execution
# Inside the function
# after Execution
# Sum = 3

# In the above example, you may notice a keen difference in the parameters of the inner function.
# The inner function takes the argument as *args and **kwargs which means that a tuple of positional
# arguments or a dictionary of keyword arguments can be passed of any length.
# This makes it a general decorator that can decorate a function having any number of arguments.


# Chaining Decorators
# In simpler terms chaining decorators means decorating a function with multiple decorators.

# code for testing decorator chaining
# code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

print(num())


# Output
# 400
# The above example is similar to calling the function as –
# decor1(decor(num))
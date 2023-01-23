# what if we want to send multiple number of arguments to a function
# in that case we define our parameter as a variable with plural name
# to indicate that it is a collection of arguments and prefix it with an '*'

def multiply(*numbers):
    print(numbers)      # we get a tuple this as output (2, 3, 4, 5)
    # tuples are also iterable
    total = 1
    for number in numbers:
        total *= number

    return total


print(multiply(2, 3, 4, 5))


# variation of this syntax
# when we use '**' before a parameter name
# we can pass multiple key-value pairs or multiple keyword arguments to the function

# Function to save information about a user
def save_user(**user):
    print(user)     # creates a dictionary object with key value pairs
    print(user["id"])   # we can also access the values of each key


# Here we are passing 3 Keyword Arguments to this function.
save_user(id=1, name='John', age=22)
# {'id': '1', 'name': 'John', 'age': 22} This will return a dictionary, witch is a complex object.


# #######################################################################################
# More Examples:

# Example 1:
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Output
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : GeeksforGeeks


# Example 2:
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)

# Now we can use *args or **kwargs to pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)

# Output
# arg1: Geeks
# arg2: for
# arg3: Geeks
# arg1: Geeks
# arg2: for
# arg3: Geeks


# Example 3:
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

# Output
# args: ('geeks', 'for', 'geeks')
# kwargs: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}


# Example 4:
class car():  # defining car class
	def __init__(self, *args):  # args receives unlimited no. of arguments as an array
		self.speed = args[0]  # access args index like array does
		self.color = args[1]


# creating objects of car class

audi = car(200, 'red')
bmw = car(250, 'black')
mb = car(190, 'white')

print(audi.color)
print(bmw.speed)

# Output
# red
# 250


# Example 5
class car():  # defining car class
	def __init__(self, **kwargs):  # args receives unlimited no. of arguments as an array
		self.speed = kwargs['s']  # access args index like array does
		self.color = kwargs['c']


# creating objects of car class

audi = car(s=200, c='red')
bmw = car(s=250, c='black')
mb = car(s=190, c='white')

print(audi.color)
print(bmw.speed)

# Output
# red
# 250

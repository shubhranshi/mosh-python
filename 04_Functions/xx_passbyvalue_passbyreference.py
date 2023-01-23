# Pass by Reference or pass by value
# One important thing to note is, IN PYTHON EVERY VARIABLE NAME IS A REFERENCE.
# When we pass a variable to a function, a new reference to the object is created.
# Parameter passing in Python is the same as reference passing in Java.

# Here x is a new reference to same list lst
def myFun(x):
	x[0] = 20


# Driver Code (Note that lst is modified after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# Output
# [20, 11, 12, 13, 14, 15]


# When we pass a reference and change the received reference to something else,
# the connection between the passed and received parameter is broken.
# For example, consider the below program as follows:

def myFun(x):

	# After below line link of x with previous object gets broken.
	# A new object is assigned to x.
	x = [20, 30, 40]


# Driver Code (Note that lst is not modified after function call.)
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# Output
# [10, 11, 12, 13, 14, 15]


# Another example to demonstrate that the reference link is broken
# if we assign a new value (inside the function).

def myFun(x):

	# After below line link of x with previous object gets broken.
	# A new object is assigned to x.
	x = 20


# Driver Code (Note that lst is not modified after function call.)
x = 10
myFun(x)
print(x)

# Output
# 10



# Exercise: Try to guess the output of the following code.

def swap(x, y):
	temp = x
	x = y
	y = temp


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)

# Output
# 2
# 3
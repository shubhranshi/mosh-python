# Modifying global Mutable Objects
# Example 1: Modifying list elements without using global keyword.
# Here, we can modify list elements defined in global scope without using global keyword.
# Because we are not modifying the object associated with the variable arr, but we are modifying the
# items the list contains. Since lists are mutable data structures, thus we can modify its contents.

arr = [10, 20, 30]


def fun():
	for i in range(len(arr)):
		arr[i] += 10


print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)

# Output
# 'arr' list before executing fun(): [10, 20, 30]
# 'arr' list after executing fun(): [20, 30, 40]


# Example 2: Modifying list variable using global keyword.
# Here we are trying to assign a new list to the global variable. Thus, we need to use the global keyword
# as a new object is created. Here, if we don’t use the global keyword, then a new local variable arr will
# be created with the new list elements. But the global variable arr will be unchanged.

arr = [100, 200, 300]


def fun():
	global arr
	arr = [20, 30, 40]


print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)

# Output
# 'arr' list before executing fun(): [10, 20, 30]
# 'arr' list after executing fun(): [20, 30, 40]


# Example 3
# Global in Nested functions
# In order to use global inside a nested function, we have to declare a variable with a global keyword
# inside a nested function.

# Python program showing a use of
# global in nested function

def add():
	x = 15
	def change():
		global x
		x = 20
	print("Before making changing: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

add()
print("value of x", x)

# Output
# Before making changing:  15
# Making change
# After making change:  15
# value of x 20

# In the above example Before and after making change(), the variable x takes the value of
# local variable i.e x = 15. Outside the add() function, the variable x will take the value defined
# in the change() function, i.e x = 20. Because we have used global keyword in x to create a
# global variable inside the change() function (local scope).


# ###############################################################################

# Global variables across Python modules
# The best way to share global variables across different modules within the same program is to create
# a special module (often named config or cfg). Import the config module in all modules of your application;
# the module then becomes available as a global name. There is only one instance of each module, and so
# any changes made to the module object get reflected everywhere. For Example, sharing global variables
# across modules.

# Code 1: Create a config.py file to store global variables
x = 0
y = 0
z = "none"

# Code 2: Create a modify.py file to modify global variables
import config
config.x = 1
config.y = 2
config.z = "geeksforgeeks"
# Here we have modified the value of x, y, and z. These variables were defined in the module config.py,
# hence we have to import config module, and can use config.variable_name to access these variables.

# Create a main.py file to modify global variables
import config
import modify
print(config.x)
print(config.y)
print(config.z)

# Output
# 1
# 2
# geeksforgeeks
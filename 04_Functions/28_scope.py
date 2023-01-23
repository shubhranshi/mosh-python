# Local and Global variables

# In programming we have a very important concept called Scope.
# Scope refers to the region of the code where the variable is defined.

msg = 'i am global'     # global variable
message = 'A'           # global


def greet():
    my_msg = 'my'
    message = "a"       # local variable of greet() ,does not exist outside the scope of this function


def send_email(name):
    message = "b"       # local variable of send_email()


def lets_change():
    # here we are telling the interpreter to use the global message and not create a local
    # variable named as message, so here we overwrite the global message variable with 'c'
    global message
    message = "c"


print(message)      # the global message variable gets printed here
#print(my_msg)      ## error, cannot be accessed outside the function

greet()
send_email("groot")
lets_change()

print(message)

# it is a bad programming practice to overwrite a global variable in a function


# #####################################################################################
# #####################################################################################

# Example 1
# This function has a variable with name same as s.

def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

# Output
# Me too.
# I love Geeksforgeeks


# Example 2
# This function uses global variable s
def f():
	s += 'GFG'
	print("Inside Function", s)


# Global scope
s = "I love Geeksforgeeks"
f()

# Output
# UnboundLocalError: local variable 's' referenced before assignment


# Example 3
# Using 'global' keyword
# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)

# Output
# Python is great! GFG
# Look for Geeksforgeeks Python Section
# Look for Geeksforgeeks Python Section


# Example 4
a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# Output
# global :  1
# Inside f() :  1
# global :  1
# Inside g() :  2
# global :  1
# Inside h() :  3
# global :  3

# Difference between Syntax Error and Exceptions
# Syntax Error: As the name suggests this error is caused by the wrong syntax in the code.
# It leads to the termination of the program.
# Exceptions: Exceptions are raised when the program is syntactically correct,
# but the code resulted in an error. This error does not stop the execution of the program,
# however, it changes the normal flow of the program.

# Python program to handle simple runtime error
# Python 3

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")


# Good Practice: to capture specific exceptions

# Some of the common built-in exceptions are other than above mention exceptions are:
# IndexError	When the wrong index of a list is retrieved.
# AssertionError	It occurs when the assert statement fails
# AttributeError	It occurs when an attribute assignment is failed.
# ImportError	It occurs when an imported module is not found.
# KeyError	It occurs when the key of the dictionary is not found.
# NameError	It occurs when the variable is not defined.
# MemoryError	It occurs when a program runs out of memory.
# TypeError	It occurs when a function and operation are applied in an incorrect type.

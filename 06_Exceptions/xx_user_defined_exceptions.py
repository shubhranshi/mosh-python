# class CustomError(Exception):
#    pass

# raise CustomError("Example of Custom Exceptions in Python")

# Output: CustomError: Example of Custom Exceptions in Python

# User-Defined Exception in Python
# Exceptions need to be derived from the Exception class, either directly or indirectly.
# Although not mandatory, most of the exceptions are named as names that end in “Error”
# similar to the naming of the standard exceptions in python.



# For example, A python program to create user-defined exception
# class MyError is derived from super class Exception
class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)


try:
    raise (MyError(3 * 2))

# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)




# Example 2:

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Error")

except Networkerror as e:
    print(e.args)
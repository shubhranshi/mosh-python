# in exception handling part : we discussed how to handle an exception.
# But, we can also raise or throw exceptions in our code.

# We have a hierarchy of exceptions in built-in exceptions
# The base class (root/parent) is the BaseException, Exception class is child of this class.
# BaseException --> Exception --> ArithmeticError --> ZeroDivisionError
# Most of the times, these built-in exceptions are sufficient.
# We can also define our own custom exceptions using classes.

# This function raises an exception if we give it an invalid argument 0 or less
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")    # built-in exception
    return 10 / age


# calculate_xfactor(-1)

# If we run this program, it will crash, and we will get the error.
# And this happens because we did not handle exception properly, We did not have a "try:" block.


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# raising exceptions is costly. We can raise and handle exceptions in a better way....

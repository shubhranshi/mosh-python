# Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# Built-in Exceptions
# https://docs.python.org/3/library/exceptions.html

# Our program may encounter error and terminate.
# Usually errors happen because of programmer mistake or bad data that we get from user or
# resources that may not be available.
# It's our job to make sure that we handle such situations in our code.
# when a Process finished with exit code 0 : normal execution
# Process finished with exit code 1: this means error while execution
# handle errors/exceptions using try/except to print proper error msg
# exception is a type of error that (terminates execution of program) crashes our program.


# when handling an exception, we can optionally define a variable that includes details
# about the exception - ValueError as ex

try:
    age = int(input('Age: '))   ##can give error ValueError is a non int value is given
    income = 20000
    risk = income / age         ##ZeroDivisionError is age is 0
    print(age)
except ZeroDivisionError:       ## catch the exception
    print('Age cannot be 0.')
except ValueError as ex:              ## catch the exception
    print('Invalid value')
    print(ex)                   ## actual error msg in the exception
    print(type(ex))             ## type of exception object
else:
    print("No exception were thrown")  ## this block is executed is no exception occurs in try block
print("Execution continues....")
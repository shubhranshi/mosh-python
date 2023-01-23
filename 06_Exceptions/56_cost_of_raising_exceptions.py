# raising exceptions is costly. We can raise and handle exceptions in a better way....

# with this "timeit" function we can calculate the execution time of some python code
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")    # built-in exception
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

# instead of printing error msg, just use pass, pass statement does nothing

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None     # None is an object that represents absence of a value
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

# we pass our code to this function, to see how much execution time our code takes.
# number denotes number of times we want to execute (large number to observe difference)
print("first code = ", timeit(code1, number=10000))
print("second code = ", timeit(code2, number=10000))

# code2 is simpler than code1
# also, the execution of code2 is 3to 4 times faster than code1
# therefore, raising exceptions comes with a cost
# If we are building a simple application for few users, raising exceptions will
# not have a bad impact on the performance of our application.
# But if we are building an application where performance and scalability is important
# then, its better to raise exceptions when it is really important.
# As a general rule of thumb, we should see if we can use a simple if statement in our code
# can handle the situation... in order to avoid raising exceptions. (like in code2)
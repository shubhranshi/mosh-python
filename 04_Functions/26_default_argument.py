# All the parameters that are in the function are required by default,
# in this lecture we are going make the parameter optional.
# All the optional parameters must come after the required parameter


def increment(number, by):
    return number + by


print(increment(2, by=1))


# we can make a parameter as optional.
# Here we will make the 'by' parameter as optional

def increment_v1(number, by=1):     # 'by' parameter is made optional
    return number + by


print(increment_v1(2))      # by default 'by' parameter will take the default value as 1
print(increment_v1(2, 5))   # here 'by' is explicitly given 5, so default value is not used

# all the optional parameters should come after the required parameter

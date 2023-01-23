# returns value to the caller of the function
# if a function doesnt have a return statement, then by default, it returns None.

def square(number):
    return number * number


def sqr(number):
    print(number * number)


result = square(3)
print(result)

print(square(5))

print(sqr(5)) # returns None

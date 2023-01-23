# If you have experience in C/C++ or Java then you must be thinking about the
# return type of the function and data type of arguments. That is possible in
# Python as well (specifically for Python 3.5 and above).

# In the function add, the arguments are expected to be of type int and the return type int.
# Subtypes are accepted as arguments.
# However, Python runtime does not enforce function and variable type annotations.
# They can be used by third party tools such as type checkers, IDEs, linters, etc.

def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
    return num3
    # return 'a'    # gives no error


# Driver code
# num1, num2 = '5', '15'    # gives no error
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

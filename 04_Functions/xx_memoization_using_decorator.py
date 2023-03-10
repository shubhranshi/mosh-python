# Memoization using decorators in Python
# Recursion is a programming technique where a function calls itself repeatedly till a termination
# condition is met. Some of the examples where recursion is used are calculation of fibonacci series,
# factorial, etc. But the issue with them is that in the recursion tree, there can be chances that
# the sub-problem that is already solved is being solved again, which adds to overhead.
# Memoization is a technique of recording the intermediate results so that it can be used to avoid
# repeated calculations and speed up the programs. It can be used to optimize the programs that use
# recursion. In Python, memoization can be done with the help of function decorators.
# Let us take the example of calculating the factorial of a number.
# The simple program below uses recursion to solve the problem:

# Simple recursive program to find factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(5))
print(facto(5))  # again performing same calculation

# Output
# 120
# 120


# The above program can be optimized by memoization using decorators.

# Factorial program with memoization using decorators.
# A decorator function for function 'f' passed as parameter
memory = {}


def memoize_factorial(f):
    # This inner function has access to memory and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)


print(facto(5))
print(facto(5))  # directly coming from saved memory


# Output
# result saved in memory
# result saved in memory
# result saved in memory
# result saved in memory
# result saved in memory
# 120
# returning result from saved memory
# 120

# Explanation:
# 1. A function called memoize_factorial has been defined. Its main purpose is to store the intermediate
# results in the variable called memory.
# 2. The second function called facto is the function to calculate the factorial. It has been annotated
# by a decorator(the function memoize_factorial). The facto has access to the memory variable as a result
# of the concept of closures. The annotation is equivalent to writing,
# facto = memoize_factorial(facto)
# 3. When facto(5) is called, the recursive operations take place in addition to the storage of intermediate
# results. Every time a calculation needs to be done, it is checked if the result is available in memory.
# If yes, then it is used, else, the value is calculated and is stored in memory.
# 4. We can verify the fact that memoization actually works, please see the output of this program.

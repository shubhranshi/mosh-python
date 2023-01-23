# While coding in various competitive sites, many people must have encountered NZEC errors.
# NZEC (non zero exit code) as the name suggests occurs when your code is failed to return 0.
# When a code returns 0 it means it is successfully executed otherwise it will return some other
# number depending on the type of error.
# When the program ends and it is supposed to return “0” to indicate if finished fine and is not
# able to do so it causes NZEC. Of course, there are more cases associated with NZEC.

# Why does NZEC occur?(one example)
# In python, generally, multiple inputs are separated by commas and we read them using input() or
# int(input()), but most of the online coding platforms while testing gives input separated by space
# and in those cases, int(input()) is not able to read the input properly and shows error like NZEC.

# How to resolve?
# For Example, Think of a simple program where you have to read 2 integers and print them
# (in input file both integers are in same line). Suppose you have two integers as shown below:
# 23 45
# Instead of using :
#        n = int(input())
#        k = int(input())

# Use:
#       n, k = raw_input().split(" ")
#       n = int(n)
#       k = int(k)
# to delimit input by white spaces.



# Wrong code
n = int(input())
k = int(input())
print (n," ",k)
# The above code will work fine when the input is in 2 two different lines.
# You can test yourself. To overcome this problem you need to use split.


# Correct code
# n, k = raw_input().split(" ")
n, k = input().split(" ")       # Starting with Python 3, raw_input() was renamed to input().
n = int(n)
k = int(k)
print (n," ",k)
# list comprehension
values_list = [x * 2 for x in range(1000)]
for x in values_list:
    print(x)    # print all the numbers in values list

# A generator expression is a compact generator notation in parentheses:
# generator_expression ::=  "(" expression comp_for ")"
# A generator expression yields a new generator object.
# Its syntax is the same as for comprehensions, except that it is enclosed in parentheses
# instead of brackets or curly braces.

# if we are dealing with a large size of data, or an infinite stream of data,
# then we should not store all the data in the memory, because it is memory inefficient.
# In situation like this, we should use a generator object.
# Generators objects are iterable just like lists, and in each iteration,
# it spits out a new value. So unlike list, they dont store all values in the memory.
# Instead, they generate a new value in each iteration

values_gen = (x * 2 for x in range(1000))
print(values_gen)
# here, values is a generator object
for x in values_gen:
    print(x)


# Lets compare the memory utilization of both list and generator object
from sys import getsizeof

print("list:", getsizeof(values_list)) #list: 9016
print("gen:", getsizeof(values_gen))    #gen: 112

# and even if we change the size of the generator object, memory utilization is consistent
values_gen = (x * 2 for x in range(100000))
print("gen:", getsizeof(values_gen))    #gen: 112

# in contrast, if we change the size of list, memory utilization also increases
values_list = [x * 2 for x in range(100000)]
print("list:", getsizeof(values_list)) #list: 824456


# Conclusion: if we are dealing with a large dataset or infinite stream of data,
# use a generator expression to create a generator object. (as they do not store the items in memory)
# Therefore, we cannot get total number of items from a generator object. We can only access the
# items when we iterate over the generator object.

# print(len(value_gen)) ---> this line will give error
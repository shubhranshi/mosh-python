# The zip function return a zip object that can combines iterables into tuples
# This function returns a list of tuples.
# The ith tuple contains the ith element from each of the argument sequences or iterables.
# If the argument sequences are of unequal lengths,
# then the returned list is truncated to the length of the shortest argument sequence.


list1 = [1, 2, 3]
list2 = [10, 20, 30]

# combine the above two lists to get:
# [(1, 10), (2, 20), (3, 30)]

# we use zip() for this
# the zip() returns an iterable that can be converted into list using list()
# the zip() takes any iterable, so we can pass lists, strings, tuple

print(list(zip("abc", list1, list2)))

# gives output : [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

zipped = zip('abc',list1,list2)
print(zipped)
l1, l2, l3 = zip(*zipped)
print(l1)
print(l2)
print(l3)
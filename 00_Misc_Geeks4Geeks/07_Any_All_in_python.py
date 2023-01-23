# https://www.geeksforgeeks.org/any-all-in-python/?ref=lbp
# Any and All are two built ins provided in python used for successive And/Or.

# Any
# Returns true if any of the items is True. It returns False if empty or all are false.
# Any can be thought of as a sequence of OR operations on the provided iterables.
# It short circuit the execution i.e. stop the execution as soon as the result is known.

# Since all are false, false is returned
print (any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))


# All
# Returns true if all of the items are True (or if the iterable is empty).
# All can be thought of as a sequence of AND operations on the provided iterables.
# It also short circuit the execution i.e. stop the execution as soon as the result is known.

# Here all the iterables are True so all
# will return True and the same will be printed
print (all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
print (all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
print (all([False, False, False]))



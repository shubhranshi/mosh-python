# For strings in python, boolean operators (and, or, not) work.

# repr()    returns the canonical string representation of the object

# The output of the boolean operations between the strings depends on the following things:
# 1. Python considers empty strings as having a boolean value of the ‘false’ and non-empty strings
# as having a boolean value of ‘true’.
# 2. For the ‘and’ operator if the left value is true, then the right value is checked and returned.
# If the left value is false, then it is returned
# 3. For the ‘or’ operator if the left value is true, then it is returned, otherwise, if the left value
# is false, then the right value is returned.

str1 = ''
str2 = 'geeks'

# repr is used to print the string along with the quotes

# Returns str1
print(repr(str1 and str2))  # ''

# Returns str1
print(repr(str2 and str1))  # ''

# Returns str2
print(repr(str1 or str2))   # 'geeks'

# Returns str2
print(repr(str2 or str1))   # 'geeks'

str1 = 'for'

# Returns str2
print(repr(str1 and str2))  # 'geeks'

# Returns str1
print(repr(str2 and str1))  # 'for'

# Returns str1
print(repr(str1 or str2))   # 'for'

# Returns str2
print(repr(str2 or str1))   # 'geeks'

str1='geeks'

# Returns False
print(repr(not str1))

str1 = ''

# Returns True
print(repr(not str1))



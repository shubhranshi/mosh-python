# Arrays are more efficient than lists when dealing with large sequence of numbers
# they perform better in memory.
# Only use arrays when encounter performance problems, otherwise, use List or Tuples

from array import array

# This module defines an object type which can compactly represent an array of basic values:
# characters, integers, floating point numbers.
# Arrays are sequence types and behave very much like lists,
# except that the type of objects stored in them is constrained.
# The type is specified at object creation time by using a type code, which is a single character.
# The following type codes are defined: https://docs.python.org/3/library/array.html

# typecode: determines the type of objects in your list/array; "i" denotes int
# if we try to put any other type of element in this array, we get error

numbers = array("i", [1, 8, 3])
print(numbers[0])
numbers.append(4)
numbers.insert(0,5)
numbers.pop(2)
numbers.remove(4)
print(numbers)

# numbers[0] = 1.0    # we get typeerror

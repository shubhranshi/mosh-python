# We are going to take a look at NumPy package. Which is heavily use in scientific computation.
# It is a package to work with Data Science and Machine Learning.
# To work with large array and multi dimension arrays, numpy is the best package

# We are importing "numpy" as an alias "np". So it is shorter to write in our code.
import numpy as np

# To create a NumPy array
array_1 = np.array([1, 2, 3])
print(array_1)
print(type(array_1)) # This is a NumPy array.

# To create a multi-dimension NumPy array. That it is called a matrix in math.
array_2 = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2)
print(array_2.shape) # With the shape attribute. We can get a tuple with the number of row and columns in our array.

# With the ".zeros()" method we can initialize a multi-dimension array of zeros.
array_zeros = np.zeros(shape=(4, 4), dtype=int)
print(array_zeros)

# With the ".ones()" method we can initialize a multi-dimension array of ones.
array_ones = np.ones(shape=(4, 4), dtype=int)
print(array_ones)

# With the ".full()" method we can initialize a multi-dimension array with a specific number "fill_value".
array_n = np.full(shape=(4, 4), fill_value=5)
print(array_n)

# We can initialize a random array, with values between 0.0 to 1.0 with the ".random()" method
# from the "random" module of NumPy.
array_rand = np.random.random((4, 4))
print(array_rand)

# To access a value in the array. In this case the value in row 0 and column 2.
print(array_rand[0, 2])

# This will return an array of boolean values.
print(array_rand > 0.3)

# This will return a new array with the numbers greater than 0.3
array_03 = array_rand[array_rand > 0.3]
print(array_03)

# This will sum all the number in our array
total = np.sum(array_rand)
print(total)

# This will return a new array, with the same shape, with the floor of all the numbers
array_floor = np.floor(array_rand)
print(array_floor)

# This will return a new array, with the same shape, with the ceil of all the numbers
array_ceil = np.ceil(array_rand)
print(array_ceil)

# This will return a new array, with the same shape, with the rounded numbers.
array_rounded = np.round(array_rand)
print(array_rounded)

# We can sum two array together
array_sum = array_1 + array_2
print(array_sum)

# This will add a 2 to all the numbers in the array.
array_add = array_2 + 2
print(array_add)

# Example: real life use, convert dimensions from inch to cm
dimensions_inch = np.array([10.45, 2.8, 3.9])   # we have an array of dimension in inches.
dimensions_cm = dimensions_inch * 2.54  # Here we convert the inches to cm.
print(dimensions_cm)

# As a comparison, If we do the same using normal arrays using list comprehensive:
dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]

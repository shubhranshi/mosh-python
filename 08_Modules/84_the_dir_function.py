# With this function we can get the list of attributes and method defined in an object.
# In this example, we import the esales module, so now esales is an object.
# So we can use the "." operator to access all the methods and attributes defined in this object.

# dir() function can be used for debugging.

from ecommerce.shopping import esales

print(dir(esales))  # we get all the attributes and methods defined in an object
# We will get this result:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_tax']
# As we can see above we have in the list the "calc_tax" method from the "esales.py" module.
# As well as other magic methods that are automatically created.

print(esales.__name__) # That returns the name of our module
print(esales.__package__) # To get the name of the package
print(esales.__file__) # To get the path to the file
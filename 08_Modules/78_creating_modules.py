# A module is a file.py
# We should separate our code in modules like products in a supermarket.
# Like a sections grouping products
# In this example for the following functions "cal_tax()" and "calc_shipping()"
# that are related with sales we should create a module with the name "sales.py" for example.
# The module name should follow the same conventions
# as naming variable or functions. Lower case letters and words separated with underscore.

# def cal_tax():
#     pass

# def calc_shipping():
#     pass
# define these 2 functions in "sales.py" file


# To import functions from one module we can use two ways.

# METHOD 1:

# In here we select the module and then separated by comma each of the functions.
from sales import calc_tax, calc_shipping

# Some tutorials teach to import multiple functions using an "*" "from sales import *".
# This is a bad practice because if we import everything blindly,
# some of our functions or variables in our "sales.py" module may
# override some objects with the same name in the current module.

calc_tax() # And then we can call each of the imported function in our new file
calc_shipping()


# METHOD 2:
# In this way now in the current module we have an object called sales,
# and we can use the "." operator to access the functions.
import sales # This is the second way to import a module


sales.calc_tax()
sales.calc_shipping()

# As our application grows we are going to organize it in folder.
# Separating the modules in folders for a better organization.
# Packages are also a way to organize our code.
# package is a container for one or more modules.
# In file systems terms a Packages is mapped to a directory and a module is mapped to a file.

# Here we created a directory/folder "ecommerce" and put the "shipping.py" module there.
# We have to add a "__init__.py" file to the "ecommerce" folder.
# this file indicates that the directory is a python package
# when python interpreter sees this __init__ file, it treats the directory(folder) as a Package.



# approach 1 - import entire module (everytime we have to use the lengthy name)
# To import the "shipping.py" module we have to prefix it with the name of the package.
import ecommerce.shipping

print(ecommerce.shipping.calc_shipping())
# to use any of the function in the "shipping.py" module
# we have to prefix it with the name of the package.




# APPROACH 2 - import a specific function
# This way is better because we don't need to prefix the name of the package
# everytime we want to use a function
from ecommerce.shipping import calc_shipping

print(calc_shipping())




# APPROACH 3- if we need many functions from a package
# If we have to import a lot a functions, it becomes noisy in the above method.
# We can import it like this.
from ecommerce import shipping

print(shipping.calc_shipping())
# And just use "esalesshipping" with the "." operator to access the functions in that module.
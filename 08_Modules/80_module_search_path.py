import sales
import sys

# Here we are importing the sales modules.
# When Python sees this it will look for a file with name esales.py in the current folder.
# If it's not found it will look in other predetermined directories that come with Python installation.

print(sys.path) # Here we can return the list of directories where Pyton will look for a module.
# the 1st element in this list represents the current folder.
print(sales.calc_tax())

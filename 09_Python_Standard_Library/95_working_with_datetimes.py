# datetime objects - year, month
from datetime import datetime
import time

# The datetime module supplies classes for manipulating dates and times.
# While date and time arithmetic is supported, the focus of the implementation
# is on efficient attribute extraction for output formatting and manipulation.

# This is one way to create a "datetime" object
dt1 = datetime(2022, 9, 11) # year,month,day,hour,minute,second....
print(dt1)


# The "now()" method from the "datetime" class returns the current time.
dt2 = datetime.now() # gives the current datetime
print(dt2)


# # This is a method to parse or convert a string into a "datetime" object.
# For example to convert input from a user or input from file.
dt3 = datetime.strptime("2022/09/12", "%Y/%m/%d") # we use the directives in 2nd argument
print(dt3)
# directives specify various component of this datetime string
# %Y - 4 digit year, %m - 2 digit month, %d - 2 digit day
# The detailed list of these directives can be found in https://docs.python.org/3/library/datetime.html


# With the ".fromtimestamp()" method we can convert a time stamp to "datetime" object.
dt4 = datetime.fromtimestamp(time.time())    # time.time() gives current timestamp
print(dt4)

print(f"{dt4.year}/{dt4.month}") # An example of the method available in a "datetime" object.


# this method is the opposite of the ".strptime()" method. To convert a "datetime" object into a string.
dt5 = dt4.strftime("%Y/%m")
print(dt5)


# We can also perform compare operation in "datetime" objects.
print(dt2 > dt1)
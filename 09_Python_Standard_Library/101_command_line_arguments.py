# If we want to create a Python program that expects command line arguments.
# Just like we write on cmd line: python app.py -a -b -c (.py file with some additional arguments)
# (depends on OS- python or python3 on terminal)

# import the "sys" module to use the attribute ".argv"
import sys

print(sys.argv) # here we get an array of 4 items.
# If we save this file and run it on terminal like: $python 101_command_line_arguments.py dd cc bb
# (.py file with some additional arguments, all these arguments represented as separate items)
# The "sys" module has an attribute "argv" (argument variable) that stores all this information in an array
# The first argument is always the name of the python file. So even if we dont supply additional arguments,
# it will always have one argument (file name)
# output: ['101_command_line_arguments.py', 'dd', 'cc', 'bb']


# we can give a USAGE msg for our file, if proper arguments are not supplied
if len(sys.argv) == 1:
    print("USAGE: python 101_command_line_arguments.py <password>")
else:
    password = sys.argv[1]
    print("Password:", password)

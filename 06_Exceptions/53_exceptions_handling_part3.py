# if we need access to resources in our program like file or database or network,
# we need to release/close those resources after using, so that they can be used by others.
# if we include the close() in try block, then if some exception occurs,
# the close() will not get a chance to execute.
# therefore, we can include such code in finally section, this section will be executed
# no matter if any exception occurs or not.

try:
    file = open("app.py")
    age = int(input('Age: '))
    xfactor = 10 / age
    # file.close() # closing the file. but if an exception occur in above line, remaining code will not be executed
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exception were thrown")
finally:
    file.close()    # This is a better place to release resources
    print("File closed successfully")
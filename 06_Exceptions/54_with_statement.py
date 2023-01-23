# we can use 'with' for opening any resources.
# Using this keyword, python will automatically close/release the resource after using it
# so we dont need to explicitly close it in finally section

# We have a shorter and cleaner way to achieve the same thing as the finally block.
# But it only works with certain objects.

try:
    with open("app.py") as file:    # opening a file with the "with" function and storing it in the variable file.
        print("File opened..")  # Python will automatically close that file whether we have a finally block or not
        # file.__enter__()
        # file.__exit__()
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
except FileNotFoundError:
    print("Couldn't find the file..")
else:
    print("No exception were thrown")
#finally:
#    file.close()
#    print("File closed successfully..")



# file.__enter__()
# file.__exit__()
# these are magic methods, (methods that are prefixed as '__')
# when an object has these 2 below methods, it means that the object supports
# Context Management Protocol, and we can use such object(file) with 'with' statement.
# it means, python will automatically call the exit() & release the resources after use.

# using 'with' statement, we can open multiple resources,
# and all these resources will be released automatically by python :

try:
    with open("app.py") as file, open("another.txt") as target:
        print("File opened")
except FileNotFoundError:
    print("File doesnt exists")

# Some times we can be working the several files
# with open("05 The With Statement.py") as file, open("04 Cleaning Up.py") as file2:
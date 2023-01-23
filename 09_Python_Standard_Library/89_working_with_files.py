
from pathlib import Path
from time import ctime
import shutil

path = Path("banking/name.txt")
print(path.exists())
# path = path.rename("set_name.py") # To rename a directory
# path.unlink()   # to delete
print(path.stat()) # With ".stat()" method we get a "os.stat_result" object with the following attributes
# st_size=0, # This returns the size of the file in bytes
# st_atime=1593375129, # This is the last access time
# st_mtime=1593375132, # The last modified time
# st_ctime=1593370616) # The creation time

# This time values are in second after epic. Epic is the start up time on a computer,
# and that is platform dependent.
# For example on unix systems the epic time is 01/01/1970.
# To print the human readable time we need to import the "ctime" function from the "time" module
print(ctime(path.stat().st_ctime))

path.read_bytes() # returns contents of the file as byte object for representing binary data

print(path.read_text()) # Which return the content of the file as a string.
# Using this method it is easier to read a file that the built-in "open()" function.

# Using "read_text()" is easier than using the built-in "open()" function
# with "open()" function we have to specify the filename and the mode
# open("__init__.py", "r") --> this return a file object so we need to close it
# As a best practice we use the with statement:
# with open("__init__.py", "r") as file
# In contrast, when we use read_text(), all opening/closing thing happens inside it,
# so, we dont have to worry about it.

# Similarly, we use
# path.write_text("...") to write textual data to file
# path.write_bytes()
# both these methods take care of opening and closing the file.

# However, when it comes to copying a file, this path object is not the ideal way
source = Path("banking/name.txt")
target = Path() / "copy_name.txt"

target.write_text(source.read_text())
# This seems a little bit tedious. There is a better way.

# We can use "shutil" module that includes many high level operations
# for copying and moving files and directories.
shutil.copy(source, target)

target.unlink() # To delete a file
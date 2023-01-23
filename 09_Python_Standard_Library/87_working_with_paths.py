# The path class is the foundation to work with files an directories.
# https://docs.python.org/3/library/pathlib.html

# importing from the "pathlib" module the "Path" class.
from pathlib import Path

# ABSOLUTE PATH

# path in mac
path = Path("/usr/local/bin")

# path in Windows
path = Path("C:\\Users\\user\\Desktop")    # absolute path
# we can also do it with a raw string using the "r" in the beginning.
# In a raw string the "\" it is not an escape sequence.
path = Path(r"C:\Users\user\Desktop")

# To create a path object that represents the current folder.
path_current_folder = Path()    # no path specified, means current folder


# RELATIVE PATH
# A relative path. From the current folder go to the subfolder "08_Modules/ecommerce".
relative_path = Path(r"../08_Modules/ecommerce/__init__.py")
print(relative_path)

# COMBINE PATH
# We can use the "/" to combine path objects.
combine_path = Path(r"C:\Users\user\Desktop") / Path(r"test_folder")
# We can use the "/" to combine path with a string.
combine_path = Path(r"C:\Users\user\Desktop") / "new folder"
print(combine_path)


# FEW METHODS IN PATH CLASS

print(Path.home())  # The class method home() returns the home directory of the current user
print(relative_path.exists())   # Call ".exist()" to see if a file or directory exists. Return True/False

path = Path(r"C:\Users\user\Desktop\Git-Cheat-Sheet.pdf")
print(path.is_file())   # To check if this path represent a file.
print(path.is_dir())    # To check if this path represent a directory.

print(path.name)    # this return only the file name in this path.
print(path.stem)    # this returns the file name without the extension.
print(path.suffix)  # This return only the extension of the file.
print(path.parent)  # This return the parent folders.

# This creates a new path object based in the existing path but only
# changes the name and extension of the file.
new_path = relative_path.with_name("file.txt")
print(new_path)


print(new_path.absolute()) # To get the absolute path.
# obviously this file doesnt exist yet, we are only representing its path.

# to change the extension of the file. Note, we are not renaming the file here,
# we are only representing a path object
renamefile_path = new_path.with_suffix(".doc")
print(renamefile_path)

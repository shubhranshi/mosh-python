
from pathlib import Path

path = Path("banking")

# some common methods
# path.exists() # to check if file/directory exists
# path.mkdir()  # To create a directory
# path.rmdir()  # To remove a directory
# path.rename("banking2.0") # To rename a directory

# with this method we can get the list of files and directories.
print(path.iterdir())
# This returns a generator object.
# Because we may be working with a large list of item.
# Instead of storing all tho item in the memory, We use a generator object.
# Each time we iterate over it we will get a new item.

path = Path("../08_Modules")
# With the for loop we can iterate over the generator. and get each file and folder
for p in path.iterdir():
    print(p)

# If we are not working with a large list of file and folders we can use a list comprehension,
# to store all the values in a list.
paths = [p for p in path.iterdir()]
print(paths)
# If we are working on Windows, we get a list of WindowsPath of files and directories
# If on Linux/Mac we get list of PosixPath

# If we want to create a list with only the directories.
filter_directories = [p for p in path.iterdir() if p.is_dir()]
print(filter_directories)

# If we want to filter the files:
filter_files = [p for p in path.iterdir() if p.is_file()]
print(filter_files)

# the ".iterdir()" has two limitations.
# 1. We cannot search by pattern
# 2. It does not search recursively
# To overcome this we can use the ".glob()" method. This also returns a generator.
# To search recursively we can use the ".rglob()".

print(path.glob("*.*")) # to search for all files
print(path.glob("*.py")) # to search for files with the extension ".py"

py_files = [p for p in path.glob("*.py")]
print(py_files)

# we will get all the py files in this folder and all its sub folders (recursively)
py_files = [p for p in path.rglob("*.py")]
print(py_files)
from pathlib import Path

#Absolute path: (start from root of our hard disk) C:\Program Files\Microsoft
#Relative path: (path starting from current directory) ecommerce

path1 = Path()   #no arguments - refers current directory

path2 = Path("../08_Modules/ecommerce")
print(path2.exists())   #check if path exists or not

path3 = Path("emails")
print(path3.exists())

print(path3.mkdir())    #create a directory, doesnot return anything, so None is printed
print(path3.rmdir())    #remove a directory


## we can also find all the files and directories in a given path
## useful when we want to automate something

path = Path()       #current directory
print(path.glob('*'))  # glob gets all the files and directory in the path

# the string depicts search pattern
#path.glob('*') all files and all directories
#path.glob('*.*') all files in current path and no directories
#path.glob('*.py') all files with .py extension

print(path.glob('*.py'))    #we can iterate through this generator object

for file in path.glob('*.py'):
    print(file)
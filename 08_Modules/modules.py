# a module in python is basically a file with some python code.
# we use modules to organize our code into multiple files
# instead of writing all code in one .py file, we divide it into different files,
# each file called as module. also promotes code reusability, maintainability
# modules should contain related functions and classes
# our code should be organized in function, classes, modules.

## use the module module_converters.py file (import)

import module_converters

print(module_converters.lbs_to_kg(70))

## instead of importing the complete modules, we can also select a specific function

from module_converters import kg_to_lbs

print(kg_to_lbs(55))
## we can use the function name directly now, we dont need to append
# the file name before function name


## exercise

from module_utils import find_max
numbers = [1, 4, 6, 2, 3]
print(find_max(numbers))

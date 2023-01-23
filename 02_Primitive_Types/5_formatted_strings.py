first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'      #string concatenation
msg = f'{first} [{last}] is a coder'    #formatted string (where curly braces define placeholders)

# f in formatted string can be both f or F.
# Any valid expression can be placed between these curly braces

print(message)
print(msg)


# ################################################################################
# Python Program for Formatting of Strings

# Default order
String1 = "{} {} {}".format('Geeks', 'For', 'Life')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
print("\nPrint String in order of Keywords: ")
print(String1)


# ###########################################################################
# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)  # 10000

# Formatting of Floats
String1 = "{0:e}".format(165.6458)
print("\nExponent representation of 165.6458 is ")
print(String1)  # 1.656458e+02

# Rounding off Integers
String1 = "{0:.2f}".format(1/6)
print("\none-sixth is : ")
print(String1)  # 0.17


# ##############################################################################
# A string can be left() or center(^) justified with the use of format specifiers,
# separated by a colon(:).
# String alignment
String1 = "|{:_<10}|{:*^10}|{:>10}|".format('Geeks',
										'for',
										'Geeks')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",
													2009)
print(String1)


# #####################################################################
# String Formatting in Python using %
# %d – integer %f – float %s – string %x – hexadecimal %o – octal

variable = '15'
string = "Variable as string = %s" %(variable)
print(string)

# Printing as raw data
print("Variable as raw data = %r" %(variable))

# Convert the variable to integer to check other formatting options

variable = int(variable) # Without this the below statement will give error.
string = "Variable as integer = %d" %(variable)
print(string)
print("Variable as float = %f" %(variable))

print ("Variable as hexadecimal = %x" %(variable))
print ("Variable as octal = %o" %(variable))

# printing as any string or char after a mark
variable = 'r'
print ("Variable as printing with special char = %c" %(variable))
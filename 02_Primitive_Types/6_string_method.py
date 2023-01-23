import string

course = 'Python for Beginners'
len_course = len(course)    #length function
print(len_course)

# difference between function and method:
# 'print' and 'len' are functions because they are not restricted to the type of object
# whereas 'upper' 'lower' are methods because they are only applicable for string objects

print(course.upper()) #it does not modify the course string, it returns a new string
print(course)
print(course.lower())
print(course.title()) #capitalizes each word
print(course.strip())   #removes whitespaces from beginning and end of a string
print(course.lstrip())  #removes whitespaces from left of a string
print(course.rstrip())  #removes whitespaces from right of a string

#find sequence of characters in a string, return the first occurance of that string
#find is case sensitive
print(course.find('P'))
print(course.find('o'))
print(course.find('O')) #if a string does not exists it returns -1
print(course.find('tho')) #sequence of characters can also be searched


#replace characters (also case sensistive)
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

# check existance of a character (or sequence of character) in a string
print('Python' in course) # this expression returns True/False - True
print('python' in course) # False
print('python' not in course) # True

# difference between 'find' method and 'in' operator
# 'find' return the index of that character(seq of char) in the string
# 'in' operator gives a boolean value - True/False if the char(seq of char) is present in string


# ##################################################################################

# split() method
# The split() method in Python returns a list of strings after breaking the given string
# by the specified separator.
# // regexp is the delimiting regular expression;
# // limit is limit the number of splits to be made
#   str.split(regexp = "", limit = string.count(str))

line = "Geek1 \nGeek2 \nGeek3"
print(line.split())
print(line.split(' ', 1))


# ##########################################################
# String constants

print(string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)            # 0123456789
print(string.octdigits)         # 01234567
print(string.hexdigits)         # 0123456789abcdefABCDEF
print(string.whitespace)        # A string containing all characters that are considered whitespace.
print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  ##ASCII punctuation characters.


## Change cases
name = 'Geeks For Geeks'
city = 'Internet'
print(name.swapcase())  # gEEKS fOR gEEKS

print(name.isdigit())   # False
print(name.isalpha())   # False
print(name.isalnum())   # False

print(city.isalpha())   # True

print(name.startswith('Gee', 0, 5))   # True    ('string',start,end)
print(name.endswith('net'))     # False

print(name.index('For'))    # 6






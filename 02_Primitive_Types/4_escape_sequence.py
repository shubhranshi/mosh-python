# if we want to use double code in the middle of the string: 2 ways

course = 'Python "Programming'  # use single quote
course = "Python \"Programming"  # use escape sequence - prefix " with a backslash
print(course)

# escape sequence:
# # - for comments
# \" - double quote
# \' - single quote
# \\ - backslash
# \n - new line


# ##################################################3
# Escaping Double Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

# Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the use of Tab
String1 = "Hi\tGeeks"
print("\nTab: ")
print(String1)

# Using raw String to ignore Escape Sequences
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1)


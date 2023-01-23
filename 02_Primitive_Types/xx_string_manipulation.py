## Slicing

String1 = "GeeksForGeeks"
# Printing First character
print("\nFirst character of String is: ")
print(String1[0])

# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String1[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(String1[3:-2])


# ##############################################################
# Program to reverse a string
# Approach 1 : using slicing
gfg = "geeksforgeeks"
print(gfg[::-1])

# Approach 2 : using reversed and join function
gfg = "geeksforgeeks"
gfg = "".join(reversed(gfg))
print(gfg)


# ###################################################################

# Python Program to Update character of a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
list1 = list(String1)
list1[2] = 'p'
String2 = ''.join(list1)
print("\nUpdating character at 2nd Index: ")
print(String2)

#2
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)


# #####################################################################
# Python Program to Delete characters from a String

String1 = "Hello, I'm a Geek"
print("Initial String: ")
print(String1)

# Deleting a character of the String
String2 = String1[0:2] + String1[3:]
print("\nDeleting character at 2nd Index: ")
print(String2)

# Deleting a String with the use of del
del String1
# print("\nDeleting entire String: ")
# print(String1) NameError: name 'String1' is not defined


# ############################################################
# Find all duplicate characters in string

# Method 1  using dictionary/list
def find_dup_char_1(input_str):
    x = []
    for i in input_str:
        if i not in x and input_str.count(i) > 1:
            x.append(i)
    print(" ".join(x))


# Method 2  using filter
def find_dup_char_2(input_str):
    x = filter(lambda x: input_str.count(x) >= 2, input_str)
    print(' '.join(set(x)))


# Driver program
if __name__ == "__main__":
    input_str = 'geeksforgeeks'
    find_dup_char_1(input_str)
    find_dup_char_2(input_str)
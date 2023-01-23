course = 'Python for Beginners'
title = "Book's Name"
name = '"Adam" Smith'

#multiline string
doc = '''
Hello, Adam
this is my first mail.
Thank you for the book. 
'''
print(course)
print(title)
print(doc)

print(course[0]) #1st character - index 0
print(title[-2]) #2nd last character
print(title[0:3]) #character at index 0,1,2
print(title[3:]) #character from index 3 to last
print(title[:5]) #character from index 0 to 4

another = title[:] #same as title
print(another)

name = 'Jennifer'
print(name[1:-1]) #character from index 1 to second last character(-2)
print(name[::-1]) # reverses the string

print(type(5))  #int
print(type(range(3)))   #range object

#range function creates an object (it is not a list) that we can iterate over.
# in each iteration this object will spit out a new number
# iterable
for item in range(10): #0-9
    print(item)

# strings are also iterable
# in each iteration, x will hold one character
for item in 'Python':
    print(item)

# lists are also iterable
for item in ['mosh','john','sara']:
    print(item)

for item in [1,2,3,4]:
    print(item)

# we can also create our own iterable custom objects
for item in shopping_cart:
    print(item)
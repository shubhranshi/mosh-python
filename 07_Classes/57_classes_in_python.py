# A class is a blueprint for creating new objects
# An object is an instance of a class

# example
# Class: Human (this class would define all the attributes of a human)
# Object: John, Mary, Jack

## classes are used to define new types
# Basic types in python:
# Numbers, String, Boolean
# Some Complex types:
# List, Dictionaries
# user defined types:
# shopping cart - classes can be used to define them.
# class name start with capital letter

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# an object is an instance of a class. Class defines a blueprint or template for defining objects.
# we can have many objects of a class
# apart from methods, these objects can also have attributes,
# these attributes are like variables that belong to a particular object.
# point1 and point2 are completely different objects.
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
# print(point2.x) ----> this will give error, because point2 object has no attribute 'x'.


# we can check the type for this object
print(type(point1)) # <class '__main__.Point'>
# to check if an object is an instance of a given class
print(isinstance(point2, Point))    # True
print(isinstance(point2, int))    # False


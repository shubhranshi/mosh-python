

class Point:
    default_color = 'red'       # class attribute

    def __init__(self, x, y):       # constructor, x,y are instance attribute
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# if we want to modify class attributes, we should use the class name to refer it (BEST PRACTICE)
Point.default_color = "yellow"


point = Point(1, 2)
# variables are dynamic in python
point.z = 10
point.draw()
point.default_color = "blue"    # refering it using object, will only modify its value for that object.
print(point.default_color)  # we can use object to get the class attribute
print(Point.default_color)  # we can also use the class name directly to get the class attribute

# INSTANCE ATTRIBUTES
# variables x, y, & z are instance attributes, meaning that they belong to an object of a class.
# Every different point object can have different values for these attributes
# Meaning that they are completely independent of each other. Each object has its own attributes

another = Point(3, 4)
another.draw()
print(another.default_color)


# CLASS ATTRIBUTES
# But we can also define attributes at the class level, known as class attributes
# and they are the same across every instance of a class.
# For eg, Human class, all humans have 2 num_of_eyes and 1 num_of_eyes (class attributes)
# but they can have different value for eye_color, full_name (instance attributes)
# default_color variable is a class attribute
# if we change its value, the change is reflected in all instances of that class

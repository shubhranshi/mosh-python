# similar to instance attributes and class attributes,
# we have instance method and class method.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod    # decorator, to denote that this method is a class method
    def zero(cls):    # by convention, class methods have 1st parameter 'cls'(we can call it anything)
        return cls(0, 0)   # this is exactly the same as calling Point(0, 0) to create a new object
        # the diff is that if we use cls(0, 0), at runtime when we call zero() method
        # python interpreter will automatically pass a reference to the Point class, to this zero().

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point1 = Point(1, 2)
point1.draw()

# Here, __init__() and draw() are an instance method. We need object to refer/call it.
# when drawing a point we need a specific point (that is why it is instance method)
# We use class method, when we do not need an existing object.

# for eg, there are a lot of cases when we want to create a point with a initial value
# we can create a point object (with a default value) using a factory method.
point2 = Point(0, 0)
# we define a factory method zero()
point2 = Point.zero()   # zero() is a factory method, which return an object with some default values.
point2.draw()
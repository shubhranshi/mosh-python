# There are time we need to compare two objects created by a class

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point_1 = Point(100, 200)
point_2 = Point(100, 200)
point_3 = Point(200, 500)

print(point_1 == point_2) #by default FALSE, after __eq__ implementation, TRUE
# (By default) If we don't have a magic method to compare objects implemented we will get false.
# The reason we get false is that by default this comparison operator compares
# the address of this two objects in memory.
# In this case this two variables are referencing two different objects in memory
# and thats why they are not equal.
# To solve this we need a magic method:
#  def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


print(point_1 > point_3)
# If we want to compare if it is grater than, we also need to implement a magic method "__gt__"
# If we don't implement this we will get an error:
# TypeError: '>' not supported between instances of 'Point' and 'Point'
# We don't have to explicitly implement the magic method "__lt__" for < because
# Python will do it automatically as we have already implemented "__gt__" (either one of them)

# constructor is a function that gets called at the time of creating an object
# __init__ is special/magic method that is the constructor of the class


class Point:
    def __init__(self, x, y):   # constructor, init short for initialize
        self.x = x      # self means reference to the current object
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("Draw ...")
        # using self, we can read attributes of the current object
        print(f"Point ({self.x}, {self.y})")


point = Point(10,20)
print(point.x)
point.x = 11
print(point.x)
# when calling the draw method, we dont need to apply value for self parameter
# python interpreter does that by default (it references the current object)
point.draw()
point.move()


##exercise

class Person:
  def __init__(self, name):
    self.name = name

  def talk(self):
    print('Talk', self.name)


p = Person('Groot')
p.talk()

bob = Person('Bob Smith')
bob.talk()
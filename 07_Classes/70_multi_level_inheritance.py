# Multi-level can be a dangerous, and make the code to complex
# it should be limited to one or two levels

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# The class chicken is inheritance all the features of the "Bird" class, but a chicken can not fly.
class Chicken(Bird):
    pass    # pass keyword is used if we have an empty class, it just say pass.. dont worry about it


class Eagle(Bird):
    def eagle_size(self):
        print("eagle size")


e = Eagle()
print(e.age)    # The Eagle class is using the age attribute from the Animal class
e.eat() # eat() of Animal class
e.fly() # fly() of Bird class
e.eagle_size()  # eagle_size() of Eagle class

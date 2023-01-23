# inheritance is a mechanism for reusing code.

# To don't repeat the same method in several classes we can use inheritance.
# It is a mechanism that allows us to define the common functions in one classes
# and then inherit them in other classes

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    # Here the Mammal class is inheriting the function and attributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")
    def walk(self):
        print("walk")


class Fish(Animal):
    # Here the Fish class is inheriting the function and attributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")
    def swim(self):
        print("swim")


m = Mammal()
m.eat()  # the Mammal class is using eat() function from the Animal class

f = Fish()
print(f.age) # The Fish class is using the age attribute from the Animal class


# The Animal class is called the Parent or Base class
# The Fish and Mammal classes are the Child or Sub class



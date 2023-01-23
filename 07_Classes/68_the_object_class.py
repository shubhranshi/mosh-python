
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):

    def walk(self):
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")

# CHECK IF AN OBJECT IS AN INSTANCE OF A CERTAIN CLASS
m = Mammal()
print(isinstance(m, Mammal))    # True
print(isinstance(m, Animal))    # True
# We are checking if Mammal class is a subclass of Animal. It will return True.

# All classes that we have, are directly or indirectly derived from the "object" Class
# which is parent of all classes
print(isinstance(m, object))    # True
# object is a built function that creates object
o = object()

# CHECK IF A CLASS IS A SUBCLASS OF A CERTAIN CLASS
print(issubclass(Mammal, Animal))
# With the built-in function "issubclass" we can check if one class is a subclass of another.
print(issubclass(Mammal, object))
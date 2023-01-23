
class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
        print("Mammal Constructor")
        super().__init__()
        # If we don't add the super function the constructor in the Animal class will not be
        # executed because it will be replaced by this class constructor (method overriding)
        # With the super() we can access any method on the animal class

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)    # this will give error AttributeError if we do not use super()
print(m.weight)
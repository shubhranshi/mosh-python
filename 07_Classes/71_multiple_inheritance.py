# In Python a class can have multiple Base classes
# But like Multi-level Inheritance it should be used with caution.
# If not used properly it will create bug in the program

class Employee:
    def greet(self):
        print("Greet Employee")


class Person:
    def greet(self):
        print("Greet Person")


class Manager1(Employee, Person):   # can inherit from multiple classes
    pass


manager1 = Manager1()
manager1.greet()    # Greet Employee
# We will get Greet Employee, because the Employee class is called first.
# If the Employee class didn't have the greet method then the greet method
# in the person class would be called.
# The order in which these base classes are inherited will also determine the
# methods and attributes values that the child class uses.


class Manager2(Person, Employee):
    pass


manager2 = Manager2()
manager2.greet()    # Greet Person

# It is better to use multiple Inheritance, with classes small classes that have nothing in common.


# This is a better example of multiple inheritance.
class Flyer: # here we are setting a class and creating a feature for flying
    def fly(self):
        pass


class Swimmer: # here we are setting a class and creating a feature for swimming
    def swim(self):
        pass


# So the FlyingFish class can inherit the features fo the Flyer and Swimer classes.
class FlyingFish(Flyer, Swimmer):
    pass
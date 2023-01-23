
from abc import ABC, abstractmethod


# Here we are defining an abstract class with an abstract method.
# This abstract method with the decorator "@abstractmethod" defines the common feature or method
# that must be implemented in the class that derive from "UIControl()".
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


# Here we define a class deriving from "UIControl()".
class TextBox(UIControl):
    def draw(self):
        print("TextBox")


# Here we define another class deriving from "UIControl()".
class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# Here we also have a function called draw, that takes a control object and
# call the draw method in that object.
# def draw(control):
#     control.draw()

# here we create a DropDownList object by instantiate the "DropDownList()" in the variable "ddl".
# Because the "DropDownList()" class derives from the class "UIControl()" the "ddl" object
# is an instance of the "UIControl()" class.
ddl = DropDownList()
print(isinstance(ddl, UIControl))

tb = TextBox()
print(isinstance(tb, UIControl))

# Here we apply the function draw in the variable "ddl" that will call the draw method from
# the "dropDownList()" class.
# draw(ddl)
# draw(tb)


# Here we would implement a function that takes an iterable like a list or a tuple and
# iterates over it with a for loop.
def draw(controls):
    for control in controls:
        control.draw()
    # In each iterations it will call the "draw()" method from
    # "DropDownList()" or "TextBox()", depending on each object it iterates.


draw([ddl, tb]) # Passing the list to the function "draw()",

# Using this approach we can render the user interface of an application
# Imagine that we have a form with Buttons, text boxes, drop down list, and so on.
# We could have a list with all this objects and pass that list to a function like the one above,
# and it would render the entire from.
# The function does not know what kind of control is working with. This is determined at runtime.
# It simples iterates over the list of controls and call the "draw()" of each control.
# This is called Polymorphism - Poly means many and morph forms - so many forms.
# To achieve Polymorphic behavior, we start by defining a base class, in this example "UIControl()"
# and there we define the common method we need in its derivatives or children.
# And then we achieve polymorphic behavior with the "draw()" function, here in line 46.
# This is how polymorphism works in pretty much all languages that support classes.

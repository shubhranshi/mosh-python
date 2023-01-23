# With the example from the last class.
# Because Python is a dynamic typed language, we do not necessarily the UIControl class


# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
       control.draw()

# With this change we can still achieve Polymorphic behavior
# In the "draw()" function on line 22, we do not specify the type of the "controls" parameter,
# it is just a label.
# We just need to pass to it an iterable object. Like a list or tuple, for example
# And each item of that object must have the "draw()" method.
# As long as this objects have a "draw()" method Python will be happy.
# This is what it is called Duck Typing. So if walks like a duck and quacks like a duck it is a duck.
# But having that "UIControl()" class its a good practice
# because it enforces a common interface in its derivatives.

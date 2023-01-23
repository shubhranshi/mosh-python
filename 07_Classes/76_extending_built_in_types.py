# In Python can also use inheritance with the built-in types.

# For example, we can create a class called "Text()" and make it a sub class of "str".
# With this our text class will inherit all the features from the "str" class.
class Text(str):
    # And we can add more feature to it. Like duplicate for example
    def duplicate(self):
        return self + self


# This text object will inherit all the features from "str"
# like ".lower()" to convert for lower case letters,
# but we can also use the new features we created in the "Text()" class.
text = Text("Python")
print(text.duplicate())


# In this example we are extending the built-in Python "list()"
# Adding features to the append method.
# Like printing this message every time an object is appended. For logging for example
# And we call the append method from the base class "List()" with the "super()" method.
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


mylist = TrackableList()
mylist.append("1")
print(mylist)

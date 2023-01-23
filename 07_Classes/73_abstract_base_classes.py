from abc import ABC, abstractmethod


class InvalidOperationError(BaseException):
    pass


class Stream(ABC):  # Deriving the Stream() class from the ABC() class we make it abstract
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # Here we solve the second issue with the abstract method.
    # Making the read() method, mandatory for all the class that derive from the Stream() class
    @abstractmethod
    def read(self):  # We just need to create the method and pass, this method has no implementation
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# continuing with the example from the last class
# There are a couple of issues with this implementation
# The first issue is that we can create a Stream object and call the "open()" method

# stream = Stream()
# stream.open()

# Why is this an issue. Because this stream class is an abstract concept.
# What are we working with a Network, File? what kind of stream?
# We should not be able to directly create an instance of the Stream() class.
# We should always sub class it. And then create an instance of the sub class,
# like FileStream() or NetworkStream() in this example.
# We just want Stream class to be base class with some common features that will be
# reused across different types of streams


# The second issue looking at the implementation of the FileStream() and NetworkStream() classes
# we have a read() method in both.
# If tomorrow we need a new class like MemoryStream(),
# it also should have the read() written in the same way.
# In other words, currently there is no way to enforce a common interface across different type
# of streams.

# to solve these problems we use an abstract base class
# importing ABC and abstractmethod, functions from the abc module.

# abstract base class is like a half baked cookie.
# if any class has abstract method, it is considered as an abstract class
# if we try to instantiate an abstract class, we will get error.

# stream = Stream() # TypeError - cant instantiate
# stream.open

# this class needs to implement abstract methods of its base class, otherwise it will also be
# considered as an abstract class. To make it instantiable (concrete class), implement read()
class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream")


stream = MemoryStream()
stream.open()
stream.read()

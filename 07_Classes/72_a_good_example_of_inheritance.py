# A good example of inheritance, would be modeling how to read a stream of data
# A stream of data can come from multiple sources, a file, network, memory etc.
# They all have features in common like opening or closing the stream.
# But how we read data from then changes from one to another.

# Creating a custom exception. By convention all custom exceptions should end with "Error".
# And every time we create a custom exception in a class,
# we should derive the exception from the base Exception.
class InvalidOperationError(Exception):
    pass


# Here we are defining a class with the common features between the streams, like open and close.
class Stream:
    def __init__(self):
        self.opened = False # Create a constructor and set an opened flag initially to false.

    # if we try to open a stream that is already opened, that an invalid operation.
    # So we can raise an exception
    def open(self):
        if self.opened:
            # Because in Python we don't have a built-in exception for this we can create a custom exception
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        # Here we check if the stream is already closed.
        # If it is closed, and we try to close it we will raise an invalid operation error.
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# This is a good example of inheritance
# We don't have multi level inheritance
# We only have two levels of inheritance
# And we don't have multiple inheritance

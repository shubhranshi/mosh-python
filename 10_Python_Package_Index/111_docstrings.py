# https://www.python.org/dev/peps/pep-0257/

# When publish our packages on Pypi repository, it is very important that we document them well for
# other people to use them.

# In this example lets say we have a class with functions to convert PDF to text.

# In python we have a special format to document our code called "Docstring", that use triple quotes """.
# Docstring (documentation string), is added right after the declaration of a class or function or variables.
# and is different from comments. Comments helps to explain "how" or "why" we have done certain things.
# Docstrings are more suitable to explain "what" a function does.


""" Module to convert PDF to text. """ # This is an example of a Docstring in the first line of the module.


class Converter:
    """ A simple converter for converting PDF to text """
    def convert(self, path):
        """
        Convert a Given PDF to text.
        Parameters:
        path (str): The path to a PDF file.
        Returns:
        str: The content of the PDF file as text.
        """
        print("PDF converted to text")


# So now when we import this module in any other python script, we will be able to see these class and
# function details (just like we see details about other modules in our editor ) when we will use them

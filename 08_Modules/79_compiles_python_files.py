#  __pychache__ it's a folder created automatically by Python for the compiled files
# In our example we have "sales.cpython-38.pyc"
# The reason Python stores this compiled files in this folder is to speed up module loading.
# The next time we run our program Python will look at the content of this folder,
# and if we have a compiled version, Python will simply load that compiled version.
# Skipping the compilation of the module. This speeds up the loading of the module,
# but not its actual performance of the application.

# Python compares the date time of the compiled version with the source code
# to check if the compiled version is up to date.
# If the date time of the source code is newer it will recompile and store it in the __pycache__
# The "cpython-38" we see in the compiled file represents
# the Python implementation used to compile this file.
# In our case it ws compiled using Python 3.8
# In this file we have Python byte code (binary form)
# Python always recompiles the module we load directly from the command line.
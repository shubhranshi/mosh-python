# In our "shipping.py" module we have few functions.
# But we can also write any statements, and they will be executed the first time that module is loaded.
# Now we add a statement there "print("Shipping initialized")"
# When we import that module Python will load that module only once and then cache it in memory.
# So the statements we write there will be executed once.
# Using the same technique we can write the code to initialize our packages in the "__init__.py" file

# In this example if we add the magic method "__name__"
# to the "print("Shipping initialized", __name__)"
# every module has a built in name attribute __name__
# Here we will see the name of the module, but if we run the file in "shipping.py"
# we will get "Shipping initialized __main__"
# The name of the module that starts our program is always "__main__"

from ecommerce import shipping

shipping.calc_shipping()


# THIS IS HOW WE CAN MAKE A FILE USABLE AS A SCRIPT, AS WELL AS A REUSABLE MODULE THAT CAN BE
# IMPORTED INTO ANOTHER MODULE.

# including below code in "shipping.py" module.
# With this sentence we can use this file as a script.
# The code we write in the if statement will not be executed
# when we import this module to another module.
# if __name__ == "__main__":
#     print("Shipping is now initialized")
#     calc_shipping()
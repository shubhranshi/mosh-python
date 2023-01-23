# Decorators with parameters is similar to normal decorators.
# The syntax for decorators with parameters :
'''
@decorator(params)
def func_name():
    """Function implementation"""
'''
# The above code is equivalent to
'''
def func_name():
    """Function implementation"""

func_name = (decorator(params))(func_name)
'''

# As the execution starts from left to right decorator(params) is called which returns a function object
# fun_obj. Using the fun_obj the call fun_obj(fun_name) is made. Inside the inner function, required
# operations are performed and the actual function reference is returned which will be assigned to func_name.
# Now, func_name() can be used to call the function with decorator applied on it.

# How Decorator with parameters is implemented

def decorators(*args, **kwargs):
	def inner(func):
		'''
		do operations with func
		'''
		return func
	return inner #this is the fun_obj mentioned in the above content

@decorators(params)
def func():
	"""
		function implementation
	"""

### REFER THIS FOR DETAILED EXPLANATION & EXAMPLE
### https://www.geeksforgeeks.org/decorators-with-parameters-in-python/?ref=lbp

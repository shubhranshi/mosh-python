# Here we will see how to call external program from our python script.
# This is particularly useful as part of an automation script. For eg lets say
# we want our Python program to run the "ls"(on mac/linux) or "dir"(windows) command and capture the output.
# We will see how to run any Operating System commands as well as external programs.
# We can have our python script execute another python script. python other.py


import subprocess
from pathlib import Path
# We need to import the "subprocess" module. With this module we can spawn a child process.
# A process is basically an instance of a running program. so with this module we can run other programs.

# subprocess.call()
# subprocess.check_call()
# subprocess.check_output()
# All these above methods are helper function to create an instance of Popen class. Also these are legacy methods.

# There is a better and newer approach subprocess.run() method.
completed = subprocess.run(["dir"],
                           shell=True,
                           capture_output=True,
                           text=True)   # The first argument to the ".run()" is an array of strings,
# that will be the command. # In Windows OS we should set shell to true.
# If we set "capture_output=True" the output will not be printed on the terminal,
# instead it will be available in the ".stdout" attribute.
# Tf we set "text=True" the output will be converted from a binary to string. And we can save it to a file.

print(type(completed))  # it is an instance of <class 'subprocess.CompletedProcess'> which has below attributes
print("Args: ", completed.args) # args is an array including the command we executed
print("Return Code: ", completed.returncode)    # 0 means success, any non-zero value indicate an error.
print("Standard error: ", completed.stderr)     # because we dont have any error, stderr is None
print("Standard output: ", completed.stdout)     # because the output is not captured, so stdout is None,
# if we set capture_output True, the output will be stored in this attribute


# Now in another example we are going to run another Python script - other.py

completed = subprocess.run(["python", Path("other.py")],
                           shell=True,
                           capture_output=True,
                           text=True)
print("Args: ", completed.args)
print("Return Code: ", completed.returncode)
print("Standard error: ", completed.stderr)
print("Standard output: ", completed.stdout)

# We are executing this other Python script as a child process.
# So it will be in a completely different memory space.
# This is different from importing that script and executing it here.
# This two scripts will be in two different process and will not share the same variables.


# Here, we will use the command "false" to force an error. So we can place the code in a "try block".

try:
    completed = subprocess.run(["false"],
                               shell=True,
                               capture_output=True,
                               text=True,
                               check=True) # If we set "check=True" this will raise an exception
    print("Args: ", completed.args)
    print("Return code: ", completed.returncode)
    print("Standard error: ", completed.stderr)
    print("Standard output", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)

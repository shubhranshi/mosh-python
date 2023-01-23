# "time" module gives us the timestamp
import time

# This time module has a method called ".time()" that returns the current day time as a timestamp
# This return a time stamp in seconds. Counting from the beginning of time in computers the epoch time.
print(time.time()) # represents number of seconds from the beginning of time (on our machine-Windows)
# We generally use timestamps for calculation (they not human readable..not formatted)


# In ths example we define a function to send emails, 1000000 e-mails
# With the code bellow we can measure how long it take to run

def send_email():
    for i in range(100000):
        pass


start = time.time() # get current time
send_email()
end = time.time()   # again get current time
duration = end - start
print(duration)

# we can also use the "timeit" module to calculate the execution of a piece of code.
# Both approaches are good.

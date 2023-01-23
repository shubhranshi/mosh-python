print("Shipping initialized", __name__)

def calc_shipping():
    print("calc shipping")


# With this sentence we can use this file as a script.
# The code we write in the if statement will not be executed
# when we import this module to another module.
if __name__ == "__main__":
    print("Shipping is now initialized")
    calc_shipping()
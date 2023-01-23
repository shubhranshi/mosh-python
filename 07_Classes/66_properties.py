# When we want to have control over an attribute in the class.
# In this example we want to restrict the price to positive values

class Product_1:
    def __init__(self, price):
        self.set_price(price)
        # We change the constructor from "self.price = price" to the set price function

    def get_price(self):  # Here we are returning the price
        return self.__price

    # In here if we try to set the price to a negative value we will raise an exception
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value


product1 = Product_1(-50) # If we try to set the price to -50 we will throw an exception

# This is a simple solution, but it is not a Pythonic solution.


# To improve this call in a Pythonic way we should use properties "property()"
# Property is an object that sits in front of an attribute and allows us to
# get or set the value of an attribute.

class Product_2:
    def __init__(self, price):
        self.set_price(price)
        # We change the constructor from "self.price = price" to the set price function

    def get_price(self):  # Here we are returning the price
        return self.__price

    # In here if we try to set the price to a negative value we will raise an exception
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value

    price = property(get_price, set_price)  # Here we call the built-in property function
    # property function (getter , setter, delete, documentation)
    # we just pass the reference to get_price and set_price method


product2 = Product_2(50)
print(product2.price)

# product.price = -10 # If we try to set the price to -1 we will raise an exception
# print(product.price)


# but even here we can use a decorator to achieve a better looking code

class Product_3:
    def __init__(self, price):
        self.price = price
        # We change the constructor from "self.price = price" to the set price function

    # here we apply the property decorator to this method.
    # And renaming the method to the ideal name, in this case price
    @property
    def price(self):
        return self.__price

    # Here we also have to add a decorator. T
    # The name of the decorator starts with the name of the property "price" and the .setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value


product3 = Product_3(50)
print(product3.price)
product3.price = -1  # If we try to set the price to -1 we will raise an exception
print(product3.price)

# If we want to make an attribute as read-only, we can skip the setter method.

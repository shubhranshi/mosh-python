# With this module we can generate random values in python
import random
import string

# This random module has a method random() that generates a random value between 0 and 1
rand1 = random.random()     # generates a float value between 0 and 1
print(rand1)

# randint() method generates random int between 2 integers. In this case between 1 and 10
rand2 = random.randint(1, 10)
print(rand2)

# super useful method - choice(), takes an array and randomly picks one of the item
rand3 = random.choice([22, 13, 7, 10, 19, 4])
print(rand3)

rand4 = random.choice(list(range(150)))
print(rand4)

# with choices() method, we can select multiple items from the list randomly, need to supply 'k'
rand5 = random.choices([1, 2, 3, 6, 5, 4, 9, 7, 8], k=2)
print(rand5)    # gives an array with 2 random items from the above list.

# We can pass any sequence to this choices() method and will pick 'k' elements
# In case we want to generate a random password, with letter abd number.
# We need to combine all elements of the output array to a string
# We use the ".join()" method with an empty string to join all the item of the selected list
# (use "" empty string with join() method, if we use ",".join() , then it will use comma as separater to join elements)
# Import the string module

# this method will return a string with the alphabet both in lower case and upper case.
# "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string.ascii_letters)
# this method will return a string with the number from 0 to 9. "0123456789"
print(string.digits)

password = "".join(random.choices(string.ascii_letters + string.digits, k=6))   # 6 lettered random password
print(password)


# To shuffle element in array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(numbers) # With this method shuffle an array.
print(numbers)



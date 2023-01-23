# Another useful data type built into Python is the dictionary (see Mapping Types — dict).
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
# which can be any immutable type; strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;
# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# You can’t use lists as keys, since lists can be modified in place using index assignments, s
# lice assignments, or methods like append() and extend().
# It is best to think of a dictionary as a set of key: value pairs, with the requirement that
# the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}.
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
# to the dictionary; this is also the way dictionaries are written on output.
# The main operations on a dictionary are storing a value with some key and extracting the value given the key.
# It is also possible to delete a key:value pair with del.
# If you store using a key that is already in use, the old value associated with that key is forgotten.
# It is an error to extract a value using a non-existent key.
# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
# in insertion order (if you want it sorted, just use sorted(d) instead).
# To check whether a single key is in the dictionary, use the in keyword.



# to store key-value pairs, each key is unique

point = {"x": 1, "y":2}
point = dict(x=1, y=2)  # we can also use dict() function to create dictionaries
print(point["x"])
point["z"] = 4 # add a new key-value pair
print(point)

# loop over dictionary
for x in point:
    print(x)    # we get only the keys

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)    # we get both the values in a tuple, and we can unpack the values

for key, value in point.items():
    print(key, value)


customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
# print(customer["birthday"]) # gives error because this key doesnt exist

# USE get() method
print(customer.get("name"))
print(customer.get("birthday")) # just returns None, instead of giving error, safer way to retrieve.
# we can set a default value, this will be returned in case of None
print(customer.get("birthday", "Jan 1 1980"))

customer["name"] = "jack smith" # update the values in a dictionary
print(customer["name"])

# can add new key-value pair also
customer["city"] = "Paris"
print(customer["city"])

print(customer)


# to delete key-values
del customer["city"]
print(customer)

# exercise
phone = input("Phone: ")
dict = {
    "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
    "7": "Seven", "8": "Eight", "9": "Nine", "0": "Zero"
}
num_in_words = ""
for digits in phone:
    num_in_words += dict.get(digits, "!") + " "
print(num_in_words)
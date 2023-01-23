# Different looping techniques using Python data structures  are:

# Way 1: Using enumerate():
# enumerate() is used to loop through the containers printing the index number along with the value
# present in that particular index.

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)


# Way 2: Using zip():
# zip() is used to combine 2 similar containers(list-list or dict-dict) printing the values
# sequentially. The loop exists only till the smaller container ends.

questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers and print values
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))


# Way 4: Using items():
# items() performs the similar task on dictionary as iteritems()
# but have certain disadvantages when compared with iteritems().
# It is very time-consuming. Calling it on large dictionaries consumes quite a lot of time.
# It takes a lot of memory. Sometimes takes double the memory when called on a dictionary.

d = {"geeks": "for", "only": "geeks"}

# iteritems() is renamed to items() in python3
# using items to print the dictionary key-value pair
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)
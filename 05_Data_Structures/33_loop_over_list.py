# loop over list
# enumerate - to get index of each element also

letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

# another way:
# enumerate() function gives an iterable object ,and in each iteration it gives a tuple (index, item)
for letter in enumerate(letters):
    print(letter[0], letter[1])

# we can take advantage of unpacking:
for index, letter in enumerate(letters):
    print(index, letter)

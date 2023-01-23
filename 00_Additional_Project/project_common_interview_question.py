# here are some popular interview questions

######### 1 ##########
# QUES: Find the most repeated character in the text

from pprint import pprint   # for pretty printing
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)
pprint(char_frequency, width=1) #better way for printing the dictionary (more readible)
# key is the character, value is its frequency
# we cannot sort dictionary, so we need to take each key-value pair, put it in a list or tuple
# then we can sort it

char_frequency_sorted = sorted(     # sorted() takes an iterable and sorts it
    char_frequency.items(),         # items() method return all key-value pairs as tuples
    key=lambda kv: kv[1],           # key attribute tells how to sort (here lambda denotes to sort based on frequency)
    reverse=True                    # to sort in descending order. highest frequency first
)

print(char_frequency_sorted[0])     # gets the character with maximum frequency

## list
name = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
name[0] = 'Jon'     #reassign the value of 1st element
print(name)
print(name[1]) #2nd element
print(name[-1]) #last element
print(name[-2]) #second last element

#slicing
print(name[2:]) #select a range: from index 2 uptill last
print(name[2:4]) #start index 2 upto index 4-excluded (item at index 4 is not included)
print(name[:])  #all items of the list
print(name[:3]) #start of list till index 3-excluded
print(name[::2])    #every 2nd element in the list, 2 is the step here
print(name[::-1])   #all item in the list in reverse order

## Here, in print(), the original list is not modified, everytime a new list is returned

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5     # gives [0, 0, 0, 0, 0] repeat items in a list using '*'
combined = zeros + letters  # we can concat 2 lists using +
print(combined)     # list can have elements/objects of different types also
# [0, 0, 0, 0, 0, 'a', 'b', 'c']

## list function
# a list function takes a iterable and converts it into a list
numbers = list(range(30))
print(numbers)

char_in_str = list("Groot")
print(char_in_str)

print("Length of list",len(char_in_str))


## exercise: find largest number in the list
numbers = [1, 4, 6, 2, 3]
max = numbers[0]

for x in numbers:
    if x > max:
        max = x
print(max)

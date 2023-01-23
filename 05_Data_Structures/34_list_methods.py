numbers = [5, 2, 1, 7, 4]
letters = ["a", "b", "c", "d", "e", "f"]

# most of these list methods are in-place

# ADD
numbers.append(20)  # add 20 to the end of list
print(numbers)

numbers.insert(0, 10) # adds 10 to 0th index
print(numbers)

# REMOVE
numbers.remove(5) # removes first occurance of item 5 from list (useful if we dont know the index)
print(numbers)

numbers.pop() # removes the last element in the list
print(numbers)

numbers.pop(1) # removes the element at index 1 in the list
print(numbers)

del letters[0:3]    # deletes elements at index in the given range
print(letters)

letters.clear()     # empties the list
print(letters)


# FINDING ITEMS
# check existance of an item in the list,
print(numbers.index(1)) # returns index of 1st occurrence, gives error if item doesnt exist
print(50 in numbers) # return true or false
print(numbers.count(2)) # gives the count of occurrences of that number in the list


# SORT, REVERSE, COPY
print("Lets sort")
numbers.sort()
print(numbers) # in-place sorting of the list in ascending order

numbers.sort(reverse=True)  # sort in descending order
print(numbers)

new_list = sorted(numbers) # this will not modify the original list, it returns a new sorted list
# sorted(numbers,reverse=True)
print(new_list)

numbers.reverse()   # reverses the list
print(numbers)


numbers2 = numbers.copy()   # creates a copy of the list
numbers2.append(6)
print(numbers2)

# now both these 2 lists are independent

numbers.clear() # empties our list
print(numbers)
print(numbers2)

# exercise - remove duplicates in a list
num_list = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for num in num_list:
    if num not in uniques:
        uniques.append(num)
print(num_list)
print(uniques)


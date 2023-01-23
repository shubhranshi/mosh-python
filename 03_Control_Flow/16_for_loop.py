# we can use for loop to iterate over elements in a list or characters in a string.

for item in 'Python':
    print(item)

for item in ['mosh','john','sara']:
    print(item)

for item in [1,2,3,4]:
    print(item)

#range function creates an object (it is not a list) that we can iterate over.
# in each iteration this object will spit out a new number
for item in range(10): #0-9
    print(item)

for item in range(5, 10): #5-9
    print(item)

for item in range(5, 10, 2): #5,7,9 , it can also take a step value (2)
    print(item)

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

#exercise
prices = [10, 20, 30]
total_cost = 0
for item in prices:
    total_cost += item
print(f"Total cost: {total_cost}")
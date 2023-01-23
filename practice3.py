count = 0
for number in range(2, 10, 2):
    print(number)
    count +=1
print(f"We have {count} numbers")

# -----------------------------------------------

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} numbers")

# -----------------------------------------------

message = "this is going to a file"
file = open("newfile.txt", "w")
file.write(message)

# -----------------------------------------------


def addition(*numbers):
    print(numbers)
    sums = 0
    for number in numbers:
        sums += number
    return sums


value = addition(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(value)

# -----------------------------------------------


def user_info(**user):
    print(user)
    print(user["id"])
    print(type(user))


user_info(id=1, name='Groot', age=10, species='tree')

# -----------------------------------------------

my_msg = 'outside'


def see_scope():
    global my_msg
    my_msg = 'inside'


print(my_msg)
see_scope()
print(my_msg)

# -----------------------------------------------

numbers = [5, 2, 1, 7, 4]

numbers.insert(0, 10) # adds 10 to 0th index
print(numbers)

numbers.pop(3)
print(numbers)

# ----------------------------------------------

# remove duplicates in a list
num_list = [2, 2, 4, 6, 3, 4, 6, 1]

for number in num_list:
    if num_list.count(number) > 1:
        num_list.remove(number)

print(num_list)

#-------------------------------------------------
items = [
    ("A", 10),
    ("B", 5),
    ("C", 7)
]


def sort_item(item):
    return item[1]

# items.sort(key=sort_item)


items.sort(key=lambda item:item[1])
print(items)


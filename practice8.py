list1 = ['s', 'w', 'f']
list2 = [55] * 4
list3 = [[4,5], [7,8]]
combined = list1 + list2 + list3
print(combined)


print(list('rocket'))
print(list(range(9)))

list4 = [4, 5, 2, 3, 9, 1]
max = list4[0]

for i in list4:
    if i > max:
        max = i

print(max)

num1, num2, *others = list4
print(num1)
print(num2)
print(others)

for index, items in enumerate(list4):
    print(index, items)

print(list4)
del list4[0:3]
print(list4)

#print(list4.index(2))

list5 = list4.copy()
list5.append(2)
print('here')
print(list5)
print(list4)


num_list = [2, 2, 4, 6, 3, 4, 6, 1]
unq_list = list(set(num_list))
print(unq_list)

unq_list = []
for num in num_list:
    if num not in unq_list:
        unq_list.append(num)

print(unq_list)


prod_list = [('p1',20), ('p2',45), ('p3',10)]
prod_list.sort()
print(prod_list)


def cust_sort(prod):
    return prod[1]


prod_list.sort(key=cust_sort)
print(prod_list)


calc = lambda x: "Even" if x % 2 == 0 else "Odd"
print(calc(20))

str = "Geeks123Do"
filter_num = lambda x: "".join(ch for ch in x if not ch.isdigit())
print(filter_num(str))

all_sum = lambda n: sum([i for i in range(n+1)])
print(all_sum(4))

l = [3, 5, 1, 2, 8, 6]
print("positive even number")
print(list(filter(lambda i: (i % 2 == 0 and i > 0), l)))


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = [item[1] for item in items]

filtered = [item for item in items if item[1] >= 10]

print(prices)
print(filtered)

odd_sqr = [i ** 2 for i in range(1,11) if i % 2 != 0]
print(odd_sqr)
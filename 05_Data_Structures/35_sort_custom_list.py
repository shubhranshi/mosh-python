# sorting a custom list

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

items.sort()
print(items)    # no change, because python doesnt know how to sort a custom list


# therefore we define a function to sort such list
# sort on basis of its price
def sort_item(item):
    return item[1]


# we pass only the reference to this function 'sort_item', we do not call it 'sort_item()'
# when python attempts to sort this list of items, it gets each item and passes it to
# our sort function sort_item
items.sort(key=sort_item)
print(items)
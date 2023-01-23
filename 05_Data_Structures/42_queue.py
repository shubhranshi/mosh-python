# https://docs.python.org/3.8/library/collections.html#collections.deque
# Empty a queue
# FIFO : first in first out
# list can be used to implement queue

queue = [1, 2, 3]
# we remove an item from the beginning of the queue (first element of the list)
# we add element at the end of the queue (append at the end of the list)
# but in large queue, this removal of first element everytime may impact the performance.
# because when the 1st item is removed from the list, all the other elements
# needs to be shifted to the left

# so, to overcome memory computation challenges, we can use deque object

from collections import deque
queue = deque([])

# add item to queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# remove item : popleft() removes first item
queue.popleft() # this function is not present in List class, this is special function of deque class
print(queue)

# similar to lists, we can check if a queue is empty or not
if not queue:
    print("Empty")
# search for python 3 module index on google
# python has a vast range on built in modules

#random is a built-in module
import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

# randomly picking an item from the list
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


### exercise - roll a dice
import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        #value = (random.randint(1,6), random.randint(1,6))
        #return value
        return first, second   #python treats this as a tuple, so no need to explicitly make a tuple.


dice = Dice()
print(dice.roll())
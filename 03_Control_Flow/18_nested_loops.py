#generate co-ordinates

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

## generate F

numbers = [5, 2, 5, 2, 2]
for x in numbers:       #range(len(numbers))
    str = ''
    for y in range(x):     #range(numbers[x])
        str = str + 'X'
    print(str)
# x = input('symbol: ')
x = '#'
print(x * 10)
print(x + ' is a symbol')
y = 'y'
print(x, 'likes', y)

# -----------------------------------

name = 'Jennifer'
print(name[1:-1])
print(name[-2:])

s = f'{name} knows symbol "{x}"'
print(s)

print(len(name))
print(name.find('i'))
print(name.replace('e', 'E'))
print(name)

# -----------------------------------

print('---------------------------------')
print(5//3)
print(-5//3)
print(5/3)
print(-5/3)

# -----------------------------------

if "bag" > "BAG":
    print(f'B [{ord("B")}] is smaller than b [{ord("b")}]')
else:
    print(f'B [{ord("B")}] is greater than b [{ord("b")}]')

# -----------------------------------

message = "five" if 5 > 3 else "three"
print(message)

# -----------------------------------

age = 26
if 18 <= age < 45:
    print("Young")

# -----------------------------------

prices = [10, 15, 35]
total_cost = 0
for price in prices:
    total_cost += price
print(f'Total price is ${total_cost}')

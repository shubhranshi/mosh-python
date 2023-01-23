items = [
    ("A", 10),
    ("B", 5),
    ("C", 7)
]

x = list(map(lambda item:item[1], items))
print(x)

# ---------------------------------------------------

y = list(filter(lambda item:item[1]>5, items))
print(y)

# --------------------------------------------------

x = [item[1] for item in items]
y = [item for item in items if item[1]>5]

print(x)
print(y)

# -------------------------------------------------


# The Equality operator (==) is a comparison operator in Python that compare values of both
# the operands and checks for value equality.
# Whereas the ‘is’ operator is the  identity operator that checks whether both the operands
# refer to the same object or not (present in the same memory location).

# ---- EXAMPLE 1: ----
# Equality operator
a = 10
b = 10
print(a == b)
# True


print(id(a))
# 2813000247664

print(id(b))
# 2813000247664    # Both a and b is pointing to the same object

print(a is b)
True

c = a       # Here variable a is assigned to new variable c, which holds same object and same memory location

print(id(c))
# 2813000247664

print(a is c)
#True



# ---- EXAMPLE 2: ----

# python3 code to
# illustrate the
# difference between
# == and is operator
# [] is an empty list
list1 = []
list2 = []
list3 = list1
print("Example 2")

if list1 == list2:     # True
	print("True")
else:
	print("False")

if list1 is list2:    # False
	print("True")
else:
	print("False")

if list1 is list3:    # True
	print("True")
else:
	print("False")

list3 = list3 + list2

if list1 is list3:    # False, because the concatenation of two lists always produces a new list.
	print("True")
else:
	print("False")
